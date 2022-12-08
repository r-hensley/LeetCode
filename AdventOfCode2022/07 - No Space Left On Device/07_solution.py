from __future__ import annotations
from dataclasses import dataclass
from typing import Union, Optional


test_input = """$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')

@dataclass
class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"file:{self.name}"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, target_file: File):
        if self.name == target_file.name and self.size == target_file.size:
            return True


@dataclass
class Directory:
    def __init__(self, name: str,
                 contents: list[File, Directory] = None,
                 parent: Optional[Directory] = None):
        if contents is None:
            contents = []

        self.name = name
        self.contents = contents
        self.parent = parent

    def append(self, addition: Union[File, Directory]):
        if addition not in self.contents:
            self.contents.append(addition)

    @property
    def level(self):
        if self.parent:
            return self.parent.level + 1
        else:
            return 0

    @property
    def size(self) -> int:
        """Returns recursively size of all files and directories inside current directory"""
        _size = 0
        for item in self.contents:
            item_size = item.size
            _size += item_size
        return _size

    def small_files(self, target_dir: Directory = None, total_size: int = 0) -> int:
        if not target_dir:
            target_dir = self

        for item in target_dir.contents:
            if type(item) == Directory:
                item: Directory
                if item.size <= 100000:
                    total_size += item.size
                total_size = self.small_files(item, total_size)

        return total_size

    def top(self) -> Directory:
        """Jumps to the top directory"""
        cwd = self
        while cwd.name != "\\":
            cwd = cwd.parent

        return cwd

    def __getitem__(self, desired_item: str):
        for item in self.contents:
            if item.name == desired_item:
                if type(item) == File:
                    raise TypeError(f"You cannot use cd to open a File "
                                    f"(tried to open {desired_item} in {self.name}: {self.contents})")
                else:
                    item: Directory
                    return item

        raise KeyError(f"Item with desired name ({desired_item}) not found in directory {self.name}: ({self.contents})")

    def __repr__(self):
        output_s = f"~/ ({int(self.size):,})\n"

        def add_dir_to_s(d: Directory, s: str):
            for item in d.contents:
                if type(item) == File:
                    s += f"  {'  '*d.level} - {item.name} ({int(item.size):,})\n"
                else:
                    item: Directory
                    s += f"  {'  '*d.level} - {item.name}/ ({int(item.size):,})\n"
                    s = add_dir_to_s(item, s)
            return s

        s = add_dir_to_s(self, output_s)
        return s

    def __str__(self):
        return self.__repr__()

    def __contains__(self, desired_item):
        for item in self.contents:
            if type(item) == type(desired_item) and item.name == desired_item.name:
                return True

    def __eq__(self, target_dir: Directory):
        if self.name == target_dir.name and self.parent == target_dir.parent:
            return True


with open('input.txt', 'r') as f:
    real_input = f.read().splitlines()


def part_one(instructions: list[str]):
    listing = False  # True if user has called "ls" and terminal is listing dir contents
    cwd: Directory = Directory("\\", [])
    for instruction in instructions:
        if listing:
            if instruction.startswith("$ "):
                listing = False
            else:
                split_instruction = instruction.split()
                if split_instruction[0] == 'dir':
                    cwd.append(Directory(split_instruction[1], None, cwd))
                else:
                    cwd.append(File(split_instruction[1], int(split_instruction[0])))

        if not listing:
            if instruction.startswith("$ ls"):
                listing = True
            else:
                if instruction == '$ cd ..':
                    if not cwd.parent:
                        raise Exception(f"cwd.parent not defined for {cwd}")
                    cwd = cwd.parent
                else:
                    target_dir = instruction.split("$ cd ")[1]
                    cwd = cwd[target_dir]


    cwd = cwd.top()
    print("Part 1 answer:", cwd.small_files())

    total_size = cwd.size
    free_space = 70000000 - total_size
    needed_size = 30000000 - free_space
    all_dirs = []

    def add_dirs_to_list(target_dir: Directory):
        for item in target_dir.contents:
            if type(item) == Directory:
                item: Directory
                all_dirs.append(item)
                add_dirs_to_list(item)

    add_dirs_to_list(cwd)
    all_dirs.sort(key=lambda x: x.size)

    for d in all_dirs:
        if d.size > needed_size:
            print('part 2 sol:', d.size)  # 4443914
            break

    return cwd


cwd = part_one(real_input)
print(cwd)


# testdir = Directory("test")
# file1 = File("file1", 3)
# file2 = File("file2", 5)
# print(testdir.contents, file1 in testdir, file2 in testdir)
# testdir.append(file1)
# print(testdir.contents, file1 in testdir, file2 in testdir)
# testdir.append(file2)
# print(testdir.contents, file1 in testdir, file2 in testdir)



# ~/ (44,376,732)
#    - lhrfs/ (240,152)
#      - hzl.jdj (197,903)
#      - wsbpzmbq.hws (42,249)
#    - mvsjmrtn (193,233)
#    - nwh/ (834,387)
#      - bgrccm.tqh (63,077)
#      - dznccwl.bnw (69,961)
#      - pmdj/ (514,336)
#        - rlgfd.rrd (292,527)
#        - tbj.grn (68,737)
#        - wsbpzmbq.hws (153,072)
#      - rsbvj.jtd (187,013)
#    - pjsd/ (22,040,913)
#      - czzcslm/ (266,197)
#        - bvrnzhd.vzp (249,237)
#        - ssvqllt.ccv (16,960)
#      - dgwpl/ (492,311)
#        - brsbfqbm.hls (23,547)
#        - ljzrwpv/ (468,764)
#          - btnzjtlr/ (191,998)
#            - tbj.mwg (191,998)
#          - czr/ (276,766)
#            - fqg/ (276,766)
#              - llhzr.pjh (276,766)
#      - fqg/ (8,011,133)
#        - bhcg (275,942)
#        - fqg/ (2,202,734)
#          - bpbtnq/ (194,542)
#            - mtztnd.hdb (194,542)
#          - btnzjtlr.mgr (267,620)
#          - fqg.vpw (174,395)
#          - tfbfgzw/ (1,431,303)
#            - cgdlflbt/ (176,005)
#              - wsbpzmbq.hws (176,005)
#            - fqg.cqp (10,814)
#            - fztb.jzr (40,235)
#            - hzl/ (1,204,249)
#              - ccpdp/ (172,836)
#                - btnzjtlr (172,836)
#              - hgwpjvn/ (384,195)
#                - hnsrdnl.ctv (122,725)
#                - tmgpjbj (261,470)
#              - hzl/ (59,843)
#                - lffmd.fwr (59,843)
#              - pbn.rzl (203,730)
#              - tbj (88,179)
#              - zdbmfmzs.jjh (295,466)
#          - twhvbbr/ (134,874)
#            - hnsrdnl.ctv (134,874)
#        - gghdbzz/ (233,336)
#          - fqg/ (233,336)
#            - ssvqllt.ccv (233,336)
#        - hswgvpt/ (2,197,079)
#          - fwfhnbc/ (293,848)
#            - zhz.mff (293,848)
#          - hcp/ (288,118)
#            - gdndr.gwn (288,118)
#          - hnsrdnl.ctv (221,595)
#          - hzl (230,875)
#          - jbfnlc.qqn (257,695)
#          - tbj.qlc (126,050)
#          - wdlh/ (778,898)
#            - btnzjtlr.msq (227,328)
#            - hzl/ (184,779)
#              - ssvqllt.ccv (184,779)
#            - hzl.wjp (94,325)
#            - zzdfcs (272,466)
#        - hzl (75,273)
#        - lfpblmwt/ (151,071)
#          - ssvqllt.ccv (151,071)
#        - sdcwn/ (2,216,158)
#          - hzl.mvp (61,632)
#          - tbj/ (772,450)
#            - btnzjtlr/ (2,441)
#              - hnsrdnl.ctv (2,441)
#            - cwsv/ (475,046)
#              - gwr (238,930)
#              - tlzqtch (236,116)
#            - tbj (1,318)
#            - wnv (293,645)
#          - tdwc/ (906,007)
#            - btnzjtlr/ (177,427)
#              - tbj.hgf (177,427)
#            - fqg/ (241,003)
#              - dbnwzbn.flv (241,003)
#            - zgjpfj/ (487,577)
#              - fqg (249,565)
#              - tbj.csq (238,012)
#          - tnjcf/ (223,888)
#            - lljwfglp.wnb (188,504)
#            - wsbpzmbq.hws (35,384)
#          - tstqdt/ (252,181)
#            - lszhdjr/ (252,181)
#              - ssvqllt.ccv (252,181)
#        - wmrwd/ (659,540)
#          - btnzjtlr (117,914)
#          - hnsrdnl.ctv (224,916)
#          - lszhdjr/ (183,834)
#            - sdnlhh.ntt (183,834)
#          - trjm.mrw (112,511)
#          - trn (20,365)
#      - lszhdjr/ (1,216,703)
#        - gjlms/ (978,639)
#          - bbs.fhq (301,712)
#          - btnzjtlr/ (60,204)
#            - nhmc (60,204)
#          - cnvlrpbs.tqv (148,329)
#          - hzl/ (99,518)
#            - lszhdjr.stz (99,518)
#          - hzl.zps (107,466)
#          - jgflpb/ (251,545)
#            - hzl.ncm (251,545)
#          - trjm.mrw (9,865)
#        - hrwjmrwf/ (218,604)
#          - btnzjtlr.qgg (65,264)
#          - pqsn (123,207)
#          - zzdfcs (30,133)
#        - vblznslv/ (19,460)
#          - hzl (19,460)
#      - mmpf/ (310,096)
#        - dnsq (200,340)
#        - snl (109,756)
#      - wtwhzzwz/ (11,594,725)
#        - bpwjhpgr/ (1,514)
#          - mjczjz (1,514)
#        - btnzjtlr/ (209,165)
#          - lszhdjr (209,165)
#        - dgqljsbq/ (5,726,044)
#          - btnzjtlr (160,750)
#          - fqg/ (464,891)
#            - ghsdjhj/ (464,891)
#              - jqcjngn.fmf (166,720)
#              - zzdfcs (298,171)
#          - hrncl/ (1,366,961)
#            - hzl/ (242,221)
#              - drndgmgz.flz (344)
#              - zzdfcs (241,877)
#            - trjm.mrw (82,355)
#            - vrqbf/ (762,532)
#              - blf/ (68,629)
#                - wdhfbtj.ncc (68,629)
#              - pzrfw/ (520,523)
#                - hzl/ (12,677)
#                  - gvdh.ltp (12,677)
#                - mdh/ (222,003)
#                  - qbvfdv (222,003)
#                - tbj/ (285,843)
#                  - wtmcqwgp/ (285,843)
#                    - stcgrs/ (285,843)
#                      - tbj (285,843)
#              - tbj/ (173,380)
#                - mcgzmthd.mdg (173,380)
#            - wsbpzmbq.hws (261,260)
#            - wtmlmprg.whh (18,593)
#          - hzvr.ftp (5,964)
#          - jldnlddj/ (2,825,575)
#            - brdtwc.pws (57,836)
#            - fqg/ (273,621)
#              - pwjr.gwt (273,621)
#            - hzl/ (1,386,475)
#              - fqg/ (533,715)
#                - hcf.sqw (290,882)
#                - hlntl.zqg (62,759)
#                - ntgm.wjn (115,593)
#                - qwtv (64,481)
#              - tbj/ (852,760)
#                - gsvpcdm (199,421)
#                - hnsrdnl.ctv (200,467)
#                - lgqgdvwz.zdp (9,980)
#                - lqlml/ (371,701)
#                  - fdwgg.rdp (92,416)
#                  - zzdfcs (279,285)
#                - pgn (19,593)
#                - tqqbwd (51,598)
#            - lbn (140,902)
#            - qhrcm/ (558,045)
#              - trjm.mrw (278,543)
#              - zzdfcs (279,502)
#            - ssrc/ (238,789)
#              - zfvwwnhl (238,789)
#            - wsbpzmbq.hws (169,907)
#          - qdc.grf (267,082)
#          - sjpdjt.ngt (205,213)
#          - vws/ (254,394)
#            - bgfrh (249,170)
#            - ndtnt/ (5,224)
#              - qwdnzdq.rfz (5,224)
#          - wzwwqq.stp (175,214)
#        - fqg/ (171,994)
#          - trjm.mrw (171,994)
#        - mbbtzgmf/ (313,256)
#          - cfqzlgm/ (232,962)
#            - tlbgq/ (232,962)
#              - ssvqllt.ccv (232,962)
#          - ssvqllt.ccv (57,211)
#          - tbj/ (23,083)
#            - lszhdjr.lzt (23,083)
#        - vvmzhhtv/ (150,567)
#          - fcpv.vws (150,567)
#        - wglhbp/ (4,443,914)    < -------- THIS WAS REMOVED
#          - cjm/ (300,643)
#            - jhtjsn.hzm (300,643)
#          - gjhzw/ (508,231)
#            - hwlj/ (280,279)
#              - ssvqllt.ccv (280,279)
#            - tbj/ (227,952)
#              - ssvqllt.ccv (88,746)
#              - tbj (139,206)
#          - lmzzlp/ (808,429)
#            - btnzjtlr (9,261)
#            - fqg/ (208,781)
#              - dcglqd.zrj (35,303)
#              - mvzh (71,812)
#              - ssvqllt.ccv (32,361)
#              - zzdfcs (69,305)
#            - fqg.fsf (128,118)
#            - hnsrdnl.ctv (165,323)
#            - prvmm/ (296,946)
#              - zzdfcs (296,946)
#          - lszhdjr.hcj (123,986)
#          - lwbz (275,863)
#          - snnhqgp.tdj (121,332)
#          - stngv/ (892,241)
#            - hgj/ (713,324)
#              - dhwr.mvc (289,819)
#              - dvpvhhgj.fmw (85,418)
#              - fqg.frj (108,543)
#              - pwhwmctv (229,544)
#            - vlb.ztz (46,259)
#            - zstwl.wgs (25,946)
#            - zzdfcs (106,712)
#          - wdzvcfm/ (84,638)
#            - sdphr/ (84,638)
#              - hnsrdnl.ctv (84,638)
#          - wjqztbj/ (873,866)
#            - btnzjtlr.ldw (240,174)
#            - lszhdjr (125,567)
#            - lszhdjr.mmz (265,718)
#            - wzjcc (242,407)
#          - wzhsq/ (454,685)
#            - hzl/ (309,519)
#              - plnn.pdn (309,519)
#            - hzl.cpv (22,176)
#            - ldtwhvc.vcv (122,990)
#        - zcwmf/ (578,271)
#          - hwq/ (309,763)
#            - trjm.mrw (189,618)
#            - wsbpzmbq.hws (120,145)
#          - mztd (268,508)
#      - zzdfcs (149,748)
#    - qfrrtb/ (21,036,060)
#      - dmntr/ (1,148,162)
#        - btnzjtlr/ (244,067)
#          - jnbthqwp (153,689)
#          - tcp/ (90,378)
#            - mczzfwsz.hwf (90,378)
#        - fqg.wcw (141,598)
#        - hnsrdnl.ctv (223,036)
#        - qhwmj (96,925)
#        - ssvqllt.ccv (257,697)
#        - vmbfhldv.zgm (184,839)
#      - fqg/ (2,929,916)
#        - btq/ (2,493,513)
#          - bdnc/ (263,358)
#            - trjm.mrw (263,358)
#          - ttpj/ (1,764,775)
#            - fqg.dvq (185,501)
#            - ltmmsr.lqd (151,107)
#            - mbtqmqh/ (1,104,843)
#              - lszhdjr/ (173,189)
#                - dmc/ (173,189)
#                  - mzmr.nrj (173,189)
#              - pmwswf.lrm (184,660)
#              - tbj/ (59,531)
#                - fjqfbq (59,531)
#              - zqbss/ (425,421)
#                - btnzjtlr/ (113,619)
#                  - trjm.mrw (113,619)
#                - lszhdjr/ (297,437)
#                  - hnsrdnl.ctv (87,142)
#                  - lszhdjr/ (210,295)
#                    - jsdrvbhc/ (210,295)
#                      - hzl (210,295)
#                - sqdj (14,365)
#              - zzdfcs (262,042)
#            - sdzp.qhb (231,236)
#            - vfflgw.vrr (16,601)
#            - zbvllh.gqb (75,487)
#          - vftshfd/ (465,380)
#            - jjws/ (82,848)
#              - trjm.mrw (82,848)
#            - mvdcjgp/ (231,865)
#              - lzzl (231,865)
#            - qflcrlrm/ (150,667)
#              - btnzjtlr (150,667)
#        - fqg (51,590)
#        - gnqsnpj.vsh (176,455)
#        - mthwtst/ (26,308)
#          - lszhdjr.dbb (26,308)
#        - trhz/ (16,138)
#          - swtdz.hdt (16,138)
#        - zbpjvb/ (165,912)
#          - hnsrdnl.ctv (69,598)
#          - tbj.gpj (96,314)
#      - gpcvsbpl/ (1,315,666)
#        - dbssfzqt/ (224,791)
#          - jcv (156,599)
#          - zzdfcs (68,192)
#        - pgn/ (782,079)
#          - fqg (124,613)
#          - gmnqvlbb.nnf (139,219)
#          - hnsrdnl.ctv (177,527)
#          - hzl.qwm (116,238)
#          - tbj/ (154,906)
#            - hnsrdnl.ctv (78,863)
#            - lszhdjr/ (76,043)
#              - qjwjw.dbn (76,043)
#          - zzdfcs (69,576)
#        - zfgvldv/ (308,796)
#          - tbj/ (308,796)
#            - gqcw.fsm (308,796)
#      - hzl/ (1,548,627)
#        - btnzjtlr (50,784)
#        - gjbcgphh.rbw (19,755)
#        - lncnj.bct (169,847)
#        - mbrtgl (46,359)
#        - nlnt/ (992,187)
#          - cqfzqwr/ (213,009)
#            - trjm.mrw (213,009)
#          - dghdql/ (61,202)
#            - hnsrdnl.ctv (61,202)
#          - fnd/ (237,330)
#            - hnsrdnl.ctv (237,330)
#          - hnsrdnl.ctv (159,573)
#          - lszhdjr/ (222,813)
#            - ssvqllt.ccv (222,813)
#          - tsm (16,814)
#          - wsbpzmbq.hws (59,202)
#          - zlbj (22,244)
#        - wfg.cdn (269,695)
#      - mqbhs/ (135,359)
#        - fqg/ (135,359)
#          - lcwsbvw.jlj (121,590)
#          - zzdfcs (13,769)
#      - pgvngj/ (414,382)
#        - lnfsw.mvd (29,079)
#        - tbj/ (385,303)
#          - ssvqllt.ccv (303,514)
#          - wsbpzmbq.hws (81,789)
#      - pnrdwlqn/ (9,650,158)
#        - btnzjtlr.hdq (145,498)
#        - fqg (209,811)
#        - gscsq/ (1,829,520)
#          - btnzjtlr/ (921,864)
#            - fqg.bcq (52,870)
#            - hnsrdnl.ctv (131,279)
#            - hts/ (295,829)
#              - hnsrdnl.ctv (295,829)
#            - plgqz.lfz (180,154)
#            - ssvqllt.ccv (118,677)
#            - zzdfcs (143,055)
#          - cmflqncq.csp (257,666)
#          - lszhdjr.jvl (146,453)
#          - ssvqllt.ccv (21,252)
#          - vjpgs/ (452,658)
#            - fqg.rjw (247,444)
#            - hzl/ (91,966)
#              - ppff.qhn (91,966)
#            - tbj (113,248)
#          - zjgswm.zmw (29,627)
#        - jbln.grc (39,287)
#        - lszhdjr/ (815,682)
#          - grzs.btl (290,399)
#          - gswg (11,125)
#          - mhdfszz.pdh (110,268)
#          - mwbjshb/ (119,607)
#            - rpgml (119,607)
#          - ndtllttm/ (5,107)
#            - qsqqfpc.mzf (5,107)
#          - wsbpzmbq.hws (126,485)
#          - zzdfcs (152,691)
#        - zcj/ (6,610,360)
#          - gftzs/ (115,531)
#            - fbjj.vrn (115,531)
#          - ssvqllt.ccv (131,397)
#          - vpqvpmv/ (5,963,271)
#            - bfqpwgdc/ (1,718,455)
#              - fqg.djq (144,904)
#              - gbn/ (1,051,516)
#                - btnzjtlr/ (1,051,516)
#                  - dzsbcqjd/ (13,953)
#                    - tbj (13,953)
#                  - fqg.fcw (253,792)
#                  - fqtqsdrt.pqd (209,245)
#                  - nqvqm (303,280)
#                  - vchvvq.cft (271,246)
#              - jzz/ (234,810)
#                - ssvqllt.ccv (234,810)
#              - vtp/ (287,225)
#                - rzqfq.pvj (287,225)
#            - ffbllv (67,619)
#            - tzr/ (4,177,197)
#              - bbzlnjtc.fft (135,596)
#              - bqfz/ (661,435)
#                - fqg (137,988)
#                - lszhdjr.bwc (122,217)
#                - ssvqllt.ccv (232,293)
#                - twrtmwh.ddc (168,937)
#              - dztgr/ (23,653)
#                - qhrp.ljh (23,653)
#              - hnsrdnl.ctv (306,047)
#              - jzdzf (248,180)
#              - lszhdjr/ (1,821,401)
#                - ghqlj/ (1,058,282)
#                  - ghshmzt.srl (184,316)
#                  - nbqndwj (258,282)
#                  - ndd/ (230,780)
#                    - gvclc (152,924)
#                    - llztchwp.jjd (77,856)
#                  - tqqlnw/ (223,468)
#                    - flvdsc.zsv (4,090)
#                    - vgwfn.zjh (219,378)
#                  - trjm.mrw (68,843)
#                  - wllcqzfr.mbd (92,593)
#                - qjjvfv/ (230,606)
#                  - trjm.mrw (230,606)
#                - qsjrnq/ (532,513)
#                  - fnnbmt.dtm (252,853)
#                  - lszhdjr.rjc (279,660)
#              - mds/ (10,903)
#                - jzwjv (10,903)
#              - nmdc/ (114,234)
#                - hnsrdnl.ctv (114,234)
#              - qpmt/ (537,396)
#                - bvrzgp (171,542)
#                - hnsrdnl.ctv (129,238)
#                - tbj (137,570)
#                - vtcfq.npn (54,929)
#                - zzdfcs (44,117)
#              - wsbpzmbq.hws (126,445)
#              - zzdfcs (191,907)
#          - wdqw/ (365,621)
#            - jmvsdlv/ (224,693)
#              - flnnqz/ (224,693)
#                - flqpwqp.fwn (224,693)
#            - mjgpdcbl/ (140,928)
#              - btnzjtlr.prd (140,928)
#          - wsbpzmbq.hws (34,540)
#      - qlnwhq/ (3,893,790)
#        - btnzjtlr/ (493,921)
#          - ssrcp.chb (225,671)
#          - tbj.cfd (268,250)
#        - cbhr/ (68,468)
#          - qdqlml.qrj (68,468)
#        - cnbssw/ (1,000,466)
#          - tbj/ (812,545)
#            - hzl (307,230)
#            - jbcnnvq/ (277,047)
#              - nztsr (277,047)
#            - lssvr.gfn (228,268)
#          - zscs (187,921)
#        - dwvv/ (1,678,371)
#          - btnzjtlr (267,743)
#          - fqg/ (863,106)
#            - btnzjtlr.hjn (260,003)
#            - btnzjtlr.ndh (103,775)
#            - trjm.mrw (200,945)
#            - twpplmhh/ (298,383)
#              - tvrq/ (298,383)
#                - ssvqllt.ccv (298,383)
#          - qznpsjp (68,364)
#          - wdr/ (248,357)
#            - tbj (248,357)
#          - wsbpzmbq.hws (230,595)
#          - wtwwd.jnb (206)
#        - lszhdjr/ (259,605)
#          - lszhdjr.mvw (259,605)
#        - rnhnbs/ (297,597)
#          - hnsrdnl.ctv (297,597)
#        - sdhqp/ (95,362)
#          - wsbpzmbq.hws (95,362)
#    - zzdfcs (31,987)
#
#