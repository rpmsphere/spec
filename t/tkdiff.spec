%define tar_ver	%(echo %{version}|sed -e 's/\\./\\-/g')

Name:		tkdiff
Version:	5.5.3
Release:	1
Summary:	A tcl/tk based graphical interface to the DIFF utility
License:	GPLv2
Group:		Development/Other
URL:		https://tkdiff.sourceforge.net/
Source0:	https://sourceforge.net/projects/tkdiff/files/%{name}/%{version}/%{name}-%{tar_ver}.zip
# desktop, icon and man files are provided from ALT linux distribution.
Source1:	tkdiff.desktop
Source2:	tkdiff.png
Source3:	tkdiff.1
BuildArch:	noarch
Requires:	diffutils
Requires:	tk

%description
tkdiff is a graphical front end to the diff program. It provides a side-by-side
view of the differences between two files, along with several innovative
features such as diff bookmarks and a graphical map of differences for quick
navigation.

%prep
%setup -q -n %{name}-%{tar_ver}
chmod 0644 README.txt

%build

%install
# binary-repertory
mkdir -p %{buildroot}%{_bindir}
install -m 0755 tkdiff %{buildroot}%{_bindir}/%{name}

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

# icons-repertory
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# man-repertory
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 %{SOURCE3} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.5.3
- Rebuilt for Fedora
* Mon Mar 21 2022 umeabot <umeabot> 5.2.1-2.mga9
+ Revision: 1814269
- Mageia 9 Mass Rebuild
* Tue Mar 30 2021 daviddavid <daviddavid> 5.2.1-1.mga9
+ Revision: 1711845
- new version: 5.2.1
* Mon Mar 08 2021 daviddavid <daviddavid> 5.2-1.mga9
+ Revision: 1700708
- new version: 5.2
* Mon Jun 15 2020 daviddavid <daviddavid> 5.0-1.mga8
+ Revision: 1593372
- new version: 5.0
+ danf <danf>
- Switch URLs from http: to https:
* Wed Feb 12 2020 umeabot <umeabot> 4.3.5-3.mga8
+ Revision: 1508193
- Mageia 8 Mass Rebuild
* Fri Sep 21 2018 umeabot <umeabot> 4.3.5-2.mga7
+ Revision: 1291853
- Mageia 7 Mass Rebuild
* Thu Aug 23 2018 daviddavid <daviddavid> 4.3.5-1.mga7
+ Revision: 1253534
- new version: 4.3.5
* Sun Jul 01 2018 daviddavid <daviddavid> 4.3.2-1.mga7
+ Revision: 1241073
- new version: 4.3.2
* Fri Jun 29 2018 daviddavid <daviddavid> 4.3.1-1.mga7
+ Revision: 1240664
- new version: 4.3.1
* Thu Jun 14 2018 daviddavid <daviddavid> 4.3-1.mga7
+ Revision: 1236829
- new version: 4.3
* Tue Feb 02 2016 umeabot <umeabot> 4.2-4.mga6
+ Revision: 931724
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 4.2-3.mga5
+ Revision: 749245
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 4.2-2.mga5
+ Revision: 689903
- Mageia 5 Mass Rebuild
* Sun Mar 23 2014 david-david <david-david> 4.2-1.mga5
+ Revision: 606971
- imported package tkdiff
