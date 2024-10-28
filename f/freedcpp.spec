Name:           freedcpp
Version:        0.0.5
Release:        18.4
License:        GPL-2.0+
Summary:        DC++ client
URL:            https://code.google.com/p/freedcpp
Group:          Productivity/Networking/Other
Source0:        https://launchpad.net/~tehnick/+archive/tehnick/+files/%{name}_%{version}.orig.tar.gz
Source1:        freedcpp.1
# PATCH-FIX-UPSTREAM freedcpp-0.0.5-icons.patch lazy.kent@opensuse.org -- install icons to the right place
Patch0:         freedcpp-0.0.5-icons.patch
BuildRequires:  compat-openssl10-devel
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
#BuildRequires:  miniupnpc-devel
BuildRequires:  python2-scons
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libgnome-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  udisks2

%description
FreeDC++ is DC++ client based on LinuxDC++ source code.

%prep
%setup -q
%patch 0
sed -i '116d' SConstruct

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing -std=gnu++98"
scons PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
scons install FAKE_ROOT=$RPM_BUILD_ROOT
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/freedcpp.1
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%find_lang %{name}
%find_lang libdcpp

%files -f %{name}.lang -f libdcpp.lang
%doc Changelog.txt Credits.txt License.txt Readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*.*
%{_datadir}/pixmaps/%{name}.*
%doc %{_mandir}/man?/*

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.5
- Rebuilt for Fedora
* Wed Feb 29 2012 lazy.kent@opensuse.org
- Initial package created - 0.0.5.
- Patch to install icons to the right place.
- Added man page from Debian Project.
