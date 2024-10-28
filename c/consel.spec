%undefine _debugsource_packages

Summary: For assessing the confidence of phylogenetic tree selection
Name: consel
Version: 0.1
Release: 3.1
Group: Applications/Bioinformatics
License: Unknown
Source:  https://www.is.titech.ac.jp/~shimo/pub/consel/cnsls01h.tgz
URL: https://www.is.titech.ac.jp/~shimo/prog/consel/index.html

%description
Author: Hidetoshi Shimodaira <shimo@is.titech.ac.jp>

CONSEL is a program package consists of small programs written in C language.
It calculates the probability value (i.e., p-value) to assess the confidence
in the selection problem. Although CONSEL is applicable to any selection
problem, it is mainly designed for the phylogenetic tree selection. CONSEL
does not estimate the phylogenetic tree by itself, but CONSEL does read the
output of the other phylogenetic packages, such as Molphy, PAML, or PAUP*.
CONSEL calculates the p-value using several testing procedures; the bootstrap
probability, the Kishino-Hasegawa test, the Shimodaira-Hasegawa test, and the
weighted Shimodaira-Hasegawa test. In addition to these conventional tests,
CONSEL calculates the p-value based on the approximately unbiased test using
the multi-scale bootstrap technique. This newly developed method gives less
biased results than the conventional methods.

%prep
%setup -q -n %{name}

%build
cd src
sed -i 's|dprintf|mydprintf|' misc.*
sed -i 's|-Wall|-Wall -fPIE|' Makefile
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result
install -m 755 src/catass   $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/catci    $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/catmt    $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/catpv    $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/catrep   $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/consel   $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/makerep  $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/makermt  $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/randrep  $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/seqmt    $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/treeass  $RPM_BUILD_ROOT%{_bindir}
install -m 755 CHANGE.txt   $RPM_BUILD_ROOT%{_docdir}/%{name}/CHANGE.txt
install -m 755 DOSUSER.txt  $RPM_BUILD_ROOT%{_docdir}/%{name}/DOSUSER.txt
install -m 755 program.pdf  $RPM_BUILD_ROOT%{_docdir}/%{name}/program.pdf
install -m 755 program.tex  $RPM_BUILD_ROOT%{_docdir}/%{name}/program.tex
install -m 755 README.txt   $RPM_BUILD_ROOT%{_docdir}/%{name}/README.txt
install -m 755 UNIXUSER.txt $RPM_BUILD_ROOT%{_docdir}/%{name}/UNIXUSER.txt
install -m 755 example/error.log  $RPM_BUILD_ROOT%{_docdir}/%{name}/example/error.log
install -m 755 example/k10s.pa    $RPM_BUILD_ROOT%{_docdir}/%{name}/example/k10s.pa
install -m 755 example/k1.pa      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/k1.pa
install -m 755 example/mam15.lnf  $RPM_BUILD_ROOT%{_docdir}/%{name}/example/mam15.lnf
install -m 755 example/mam15.tpl  $RPM_BUILD_ROOT%{_docdir}/%{name}/example/mam15.tpl
install -m 755 example/mu1.vt     $RPM_BUILD_ROOT%{_docdir}/%{name}/example/mu1.vt
install -m 755 example/sample1.sh $RPM_BUILD_ROOT%{_docdir}/%{name}/example/sample1.sh
install -m 755 example/sample2.sh $RPM_BUILD_ROOT%{_docdir}/%{name}/example/sample2.sh
install -m 755 example/short.pa   $RPM_BUILD_ROOT%{_docdir}/%{name}/example/short.pa
install -m 755 example/sim1.vt    $RPM_BUILD_ROOT%{_docdir}/%{name}/example/sim1.vt
install -m 755 example/test.sh    $RPM_BUILD_ROOT%{_docdir}/%{name}/example/test.sh
install -m 755 example/result/mam15.ass      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15.ass
install -m 755 example/result/mam15.ci       $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15.ci
install -m 755 example/result/mam15e.ci      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15e.ci
install -m 755 example/result/mam15e.pv      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15e.pv
install -m 755 example/result/mam15e-pv.txt  $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15e-pv.txt
install -m 755 example/result/mam15.pv       $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15.pv
install -m 755 example/result/mam15-pv.txt   $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15-pv.txt
install -m 755 example/result/mam15-tree.log $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/mam15-tree.log
install -m 755 example/result/test1.txt      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/test1.txt
install -m 755 example/result/test2.txt      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/test2.txt
install -m 755 example/result/test3.txt      $RPM_BUILD_ROOT%{_docdir}/%{name}/example/result/test3.txt

%files
%{_bindir}/catass
%{_bindir}/catci
%{_bindir}/catmt
%{_bindir}/catpv
%{_bindir}/catrep
%{_bindir}/consel
%{_bindir}/makerep
%{_bindir}/makermt
%{_bindir}/randrep
%{_bindir}/seqmt
%{_bindir}/treeass
%docdir %{_docdir}/%{name}
%{_docdir}/%{name}

%changelog
* Fri Jun 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Tue Feb 22 2005 Cymon J. Cox <cymon@duke.edu>
- Rebuild for release h
* Mon Apr 5 2004 Cymon J. Cox <cymon@duke.edu>
- First build
