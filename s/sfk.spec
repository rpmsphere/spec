Name:		sfk
Version:	1.9.9
Release:	1
Summary:	Swiss File Knife
License:	BSD
Group:		File tools
URL:		https://stahlworks.com/dev/swiss-file-knife.html
Source0:	https://downloads.sourceforge.net/swissfileknife/%{name}-%{version}.tar.gz

%description
sfk ("Swiss File Knife") combines many command line tools in a single
portable executable (for e.g. search and convert text files, find
duplicate files, compare folders, treesize, run own commands on all
files of a folder).

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.9
- Rebuilt for Fedora
* Sun May 24 2020 daviddavid <daviddavid> 1.9.7-1.mga8
+ Revision: 1587262
- new version: 1.9.7
* Thu Feb 20 2020 umeabot <umeabot> 1.9.6-2.mga8
+ Revision: 1547382
- Mageia 8 Mass Rebuild
* Sun Feb 09 2020 daviddavid <daviddavid> 1.9.6-1.mga8
+ Revision: 1488097
- new version: 1.9.6
+ wally <wally>
- replace deprecated %%configure2_5x
* Sun Jun 30 2019 daviddavid <daviddavid> 1.9.5-1.mga8
+ Revision: 1416341
- new version: 1.9.5
* Tue Feb 12 2019 daviddavid <daviddavid> 1.9.4-1.mga7
+ Revision: 1365417
- new version: 1.9.4
* Sun Dec 09 2018 daviddavid <daviddavid> 1.9.3.4-1.mga7
+ Revision: 1339087
- new version: 1.9.3.4
- remove merged upstream patch
* Sat Nov 03 2018 daviddavid <daviddavid> 1.9.3.3-1.mga7
+ Revision: 1327827
- new version: 1.9.3.3
- new version: 1.9.3.2
- initial package sfk
