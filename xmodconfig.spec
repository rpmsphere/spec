%global debug_package %{nil}

Name:               xmodconfig
Version:            0.2.0
%define pkg_version 0.2.0-beta
Release:            6.1
Summary:            XModMap Configuration Frontend
Source:             xmodconfig-%{pkg_version}.tar.bz2
URL:                http://sourceforge.net/projects/xmodconfig/
Group:              System/X11/Utilities
License:            GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:      libpng-devel
BuildRequires:      qt4-devel
BuildRequires:      gcc-c++ libstdc++-devel
BuildRequires:      gcc make glibc-devel pkgconfig
BuildRequires:      autoconf automake libtool

%description
xmodconfig is a graphical front end for xmodmap. It enables you to configure
xmodmap files without using a text editor or any additional application such as
xev.

%prep
%setup -q -n "%{name}-%{pkg_version}"
find . -name '*~' -exec %__rm {} \;
sed -i 's|ok = false;|*ok = false;|' src/tooltips.cpp

%build
qmake-qt4 PREFIX="%{_prefix}"
%__make %{?jobs:-j%{jobs}} PREFIX="%{_prefix}"

%install
%__make INSTALL_ROOT="$RPM_BUILD_ROOT" PREFIX="%{_prefix}" install

LF="$PWD/%{name}.lang"
pushd "$RPM_BUILD_ROOT%{_datadir}/xmodconfig"
for f in *_*.qm *_*.ts; do
    [ -e "$f" ] || continue
    l="${f%.*}"
    l="${l#xmodconfig_}"
    echo "%lang($l) %{_datadir}/xmodconfig/$f" >>"$LF"
done
popd

%__rm -rf "$RPM_BUILD_ROOT%{_datadir}/doc"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files -f "%{name}.lang"
%doc COPYING README doc/*
%{_bindir}/xmodconfig
%{_datadir}/applications/xmodconfig.desktop
%{_datadir}/pixmaps/xmodconfig.png
%dir %{_datadir}/xmodconfig
%{_datadir}/xmodconfig/*.xml
%{_datadir}/xmodconfig/defaults
%{_mandir}/man1/xmodconfig.1*

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuild for Fedora
* Sun Aug  8 2010 pascal.bleser@opensuse.org
- update to 0.2.0:
  * a new design is used
  * a search function was added
  * tooltips were improved
  * thread safety was improved
  * the handbook was extended
  * some bugs were fixed
* Sat Jul 31 2010 pascal.bleser@opensuse.org
- new package (0.1.1+0.1.2beta)
