Summary: Cairo Gauge to display values read from your PC
Name: gauge
Version: 3.6
Release: 1
License: GPLv2
URL: https://www.theknight.co.uk/
Group: Applications/Productivity
Source: https://www.theknight.co.uk/releases/source/%{name}-%{version}.tar.bz2
BuildRequires: gtk3-devel desktop-file-utils libcurl-devel libxml2-devel json-glib-devel pango-devel zlib-devel gcc
BuildRequires: libdial libdial-devel
BuildRequires: lm_sensors-devel

%description
GTK/Cairo Gauge.

%prep
%setup -q

%build
%configure 
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 755 gauge $RPM_BUILD_ROOT%{_bindir}/gauge
install -p -m 644 icons/scalable/gauge.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/gauge.svg
install -p -m 644 icons/128x128/gauge.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/gauge.png
install -p -m 644 icons/48x48/gauge.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gauge.png
desktop-file-install --vendor="" --dir=${RPM_BUILD_ROOT}%{_datadir}/applications gauge.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/gauge
%{_datadir}/applications/gauge.desktop
%{_datadir}/icons/hicolor/scalable/apps/gauge.svg
%{_datadir}/icons/hicolor/128x128/apps/gauge.png
%{_datadir}/icons/hicolor/48x48/apps/gauge.png

%doc COPYING AUTHORS

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6
- Rebuilt for Fedora
* Mon Jan 01 2018 Chris Knight <chris@theknight.co.uk> 2.1.7-1
- New release with support for Fedora 27 and ubuntu 17.10.
* Thu Nov 17 2011 Chris Knight <chris@theknight.co.uk> 2.0.1-1
- Lots of work porting to GTK3 for Gnome 3 desktops.
* Tue Mar 09 2010 Chris Knight <chris@theknight.co.uk> 1.0.0-1
- Made suggested changes to the spec file
