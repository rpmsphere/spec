Name:		meegotouch-theme
Summary:	Theme for Meego Touch based applications
Version:	0.21.3
Release:	1.1
Group:		User Interface/Desktops
License:	LGPLv2
URL:		http://meego.gitorious.org/meegotouch/meegotouch-theme
#extracted from http://repo.meego.com/MeeGo/builds/trunk/1.0.90.1.20100907.1/core/repos/source/meegotouch-theme-0.20.29-2.5.src.rpm
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildArch:	noarch

%description
Theme required by any MeeGo Touch library based application. Contains the base
theme files and two alternative themes with a different look.

%prep
%setup -q

# Fix some wrong modes.
find -type f -exec chmod -x {} ";"

%build
qmake-qt4
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make INSTALL="install -p" INSTALL_ROOT=%{buildroot} install
mv %{buildroot}%{_datadir}/themes/base %{buildroot}%{_datadir}/themes/meegotouch
# Remove known zero-length files
find %{buildroot}%{_datadir}/themes -type f -size 0c -exec rm -f {} ';'

%files
%doc LICENSE.LGPL
%{_datadir}/themes/meegotouch

%clean
rm -rf %{buildroot}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.21.3
- Rebuilt for Fedora
* Sun May 29 2011 Jon Nordby <jonn@openismus.com> - 0.21.3-1
- Make compatible with OpenSUSE 11.4
* Tue May 24 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.21.3-0
- Update to 0.21.3
* Mon Apr 25 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.20.95-0
- Update to 0.20.95
* Wed Sep 08 2010 Chen Lei <supercyper@163.com> - 0.20.29-1
- Initial packaging for Fedora
* Mon Jun 21 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.14
- Change start priority in desktop file to Highest - BMC #3328
