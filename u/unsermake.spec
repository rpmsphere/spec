%undefine _debugsource_packages
Name:          unsermake
Version:       0.0svn20060112
Release:       4.1
Summary:       A replacement for automake
Group:         Development/Tools
URL:           https://www.kde.me.uk/index.php?page=unsermake
Source:        %{name}-%{version}.tar.bz2
License:       GPL
BuildRequires: python-devel
BuildArch:     noarch

%description
Unsermake is a replacement for automake by KDE developer Stephen Kulow.
Unsermake replaces automake and make but keeps everything else,
including the strange Makefile.am syntax the same.

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{python2_sitearch}/unsermake/
cp -a * $RPM_BUILD_ROOT%{python2_sitearch}/unsermake/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -s %{python2_sitearch}/unsermake/unsermake $RPM_BUILD_ROOT%{_bindir}/unsermake

%files
%doc COPYING README TODO
%{_bindir}/unsermake
%{python2_sitearch}/unsermake

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0svn20060112
- Rebuilt for Fedora
* Mon Jun 29 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.0svn20060112-2mamba
- specfile updated and rebuilt
* Thu Jan 12 2006 Silvan Calarco <silvan.calarco@qilinux.it> 0.0svn20060112-1qilnx
- update to version 0.0svn20060112 by autospec
* Tue Dec 20 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.0svn20050813-3qilnx
- rebuilt and sent to Qilinux-1.2 updates repository
* Sat Aug 13 2005 Silvan Calarco <silvan.calarco@qilinux.it> svn08132005-1qilnx
- added patch to fix a bash error on designer.um module build
* Sat Aug 13 2005 Silvan Calarco <silvan.calarco@qilinux.it> svn08132005-1qilnx
- package created by autospec
