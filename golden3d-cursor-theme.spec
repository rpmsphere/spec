%define dir_name    Golden-3D

Name:               golden3d-cursor-theme
Summary:            Golden 3D Cursor Theme
Version:            0.8
Release:            12.1
License:            LGPL
Group:              System/X11/Icons
Source0:            golden-3d-cursor-theme-%{version}.tar.bz2
BuildArch:          noarch
URL:                http://www.kde-look.org/content/show.php?content=5507

%description
A golden xcursors theme, modeled, animated and rendered in Blender3D.

Author:
-------
    ezteban

%prep
%setup -q -n golden-3d-cursor-theme-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{dir_name}/cursors
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -r Gold/cursors $RPM_BUILD_ROOT%{_datadir}/icons/%{dir_name}
cp default/* $RPM_BUILD_ROOT%{_datadir}/icons/%{dir_name}
cp README $RPM_BUILD_ROOT%{_docdir}/%{name}
MD5SUM=$(md5sum COPYING | sed 's/ .*//')
if test -f /usr/share/doc/licenses/md5/$MD5SUM ; then
        ln -sf /usr/share/doc/licenses/md5/$MD5SUM COPYING; else
        cp COPYING $RPM_BUILD_ROOT%{_docdir}/%{name};
    fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{dir_name}
%{_docdir}/%{name}

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora
* Wed Dec 10 2008 buschmann23@opensuse.org
- fixing some rpmlint warnings/errors
* Thu Jan 10 2008 buschmann@huessenbergnetz.de
- improve spec file
* Sat Nov 24 2007 buschmann@huessenbergnetz.de
- enhance spec file
* Sat Dec 16 2006 buschmann@huessenbergnetz.de
- initial package
