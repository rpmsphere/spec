%global __os_install_post %{nil}

Name:           fahmon
Version:        2.3.99.4
Release:        9.1
License:        GPL-2.0
Summary:        Monitor for Folding@home Clients
URL:            https://fahmon.net/
Group:          System/Monitoring
Source0:        https://fahmon.net/downloads/FahMon-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE fahmon-2.3.99.4-pixdir.patch lazy.kent@opensuse.org -- install icons into program dir, not into system one
Patch0:         fahmon-2.3.99.4-pixdir.patch
BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  wxGTK2-devel
BuildRequires:  libcurl-devel

%description
FahMon is an open-source tool (GPL license) that allows you to quickly
check the progress of your Folding@Home client (or clients if you have
multiple), avoiding you having to open different files and/or to go to
the Internet (for example to know how much your current work unit is
worth).

%prep
%setup -qn FahMon-%{version}
%patch 0
sed -i -e '52,54d' -e '80d' src/main.cpp

%build
#alternatives --set wx-config /usr/bin/wx-config-2.0
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/libwxcurl.{la,so}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TEMPLATE_SYNTAX THANKS
%doc doc/help/User_Guide.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/*.so*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.99.4
- Rebuilt for Fedora
* Mon Feb 27 2012 lazy.kent@opensuse.org
- Split off language package.
- Use defines for wxWidgets.
- Removed check for unsupported openSUSE versions.
- Use make_install macro.
* Sun Nov  6 2011 lazy.kent@opensuse.org
- Added icon_theme_cache_post/un macros.
- Corrected License tag.
- Use full URL as a source.
- spec clean up and formatting.
* Mon Apr 18 2011 lazy.kent@opensuse.org
- build requires wxWidgets-wxcontainer-devel for oS > 11.3
* Mon Mar  7 2011 lazy.kent@opensuse.org
- initial package created - 2.3.99.4
- pixdir patch
