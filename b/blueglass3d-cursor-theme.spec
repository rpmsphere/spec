%define dir_name    Blue-Glass-3D

Name:               blueglass3d-cursor-theme
Summary:            Blue Glass 3D Cursor Theme
Summary(de):        Blue Glass 3D Mauszeiger
Version:            0.4
Release:            7.1
License:            LGPL
Group:              System/X11/Icons
Source0:            blue-glass-3d-cursor-theme-%{version}.tar.bz2
BuildArch:          noarch
URL:                https://www.kde-look.org/content/show.php?content=5532

%description
A blue glass xcursors theme, modeled, animated and rendered in Blender3D.

Author:
-------
    ezteban

%prep
%setup -q -n blue-glass-3d-cursor-theme-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{dir_name}/cursors
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -r Blue/cursors $RPM_BUILD_ROOT%{_datadir}/icons/%{dir_name}
cp default/* $RPM_BUILD_ROOT%{_datadir}/icons/%{dir_name}
cp README $RPM_BUILD_ROOT%{_docdir}/%{name}
MD5SUM=$(md5sum COPYING | sed 's/ .*//')
if test -f /usr/share/doc/licenses/md5/$MD5SUM ; then
        ln -sf /usr/share/doc/licenses/md5/$MD5SUM COPYING; else
        cp COPYING $RPM_BUILD_ROOT%{_docdir}/%{name};
    fi

%files
%{_datadir}/icons/%{dir_name}
%{_docdir}/%{name}

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Wed Dec 10 2008 buschmann@huessenbergnetz.de
- fixing file list
* Thu Jan 10 2008 buschmann@huessenbergnetz.de
- improve spec file
* Sat Nov 24 2007 buschmann@huessenbergnetz.de
- enhance spec file
* Sat Dec 16 2006 buschmann@huessenbergnetz.de
- initial package
