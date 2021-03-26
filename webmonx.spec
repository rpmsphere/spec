%global debug_package %{nil}

Name:           webmonx
Version:        0.3.3
Release:        6.1
License:        GPL-2.0+
Summary:        Websites Update Monitoring Tool
URL:            http://debfx.fobos.de/webmonx/
Group:          Productivity/Networking/Web/Utilities
Source0:        http://downloads.sourceforge.net/webmonx/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM webmonx-0.3.3-fix_dir.patch lazy.kent@opensuse.org -- fix program data directory
Patch0:         webmonx-0.3.3-fix_dir.patch
# PATCH-FIX-OPENSUSE webmonx-0.3.3-optflags.patch lazy.kent@opensuse.org -- use optimization flags and don't strip binaries
Patch1:         webmonx-0.3.3-optflags.patch
# PATCH-FIX-UPSTREAM webmonx-0.3.3-gcc47.patch lazy.kent@opensuse.org -- fix compilation with GCC 4.7
Patch2:         webmonx-0.3.3-gcc47.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)

%description
WebMonX monitors websites for updates and changes - it saves you time
and always keeps you up-to-date by periodically checking these pages at
set intervals.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
qmake-qt4 \
PREFIX=%{_prefix}
QMAKE_CFLAGS+="%{optflags}" \
QMAKE_CXXFLAGS+="%{optflags}" \
QMAKE_STRIP=""
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%doc CHANGELOG LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuild for Fedora
* Fri Apr 27 2012 lazy.kent@opensuse.org
- Patch to fix compilation with GCC 4.7.
- Use pkgconfig(*) as build dependencies.
- Removed check for unsupported openSUSE versions.
* Thu Nov 10 2011 lazy.kent@opensuse.org
- Patch to use optflags.
- Added LICENSE to docs.
- Build requires hicolor-icon-theme.
- Added icon_theme_cache_post/un macros.
- Corrected License tag.
- Use full URL as a source.
- spec clean up.
* Sat Apr  3 2010 lazy.kent.suse@gmail.com
- Initial package created - 0.3.3.
- Patch to fix program data directory.
