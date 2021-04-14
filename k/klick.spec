Name:           klick
Version:        0.12.2
Release:        11.1
Summary:        An advanced JACK-based metronome
Group:          Applications/Engineering
License:        GPLv2+
URL:            http://das.nasophon.de/klick/
Source0:        http://das.nasophon.de/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  liblo-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  rubberband-devel
BuildRequires:  python2-scons <= 3.0.1

%description
klick is an advanced JACK-based metronome, supporting tempo changes,
meter changes, and more. It allows you to define complex tempo maps
for entire songs or performances.

%prep
%setup -q
sed -i 's|static double const|static double constexpr|' src/metronome_map.hh
sed -i 's|static float const|static float constexpr|' src/metronome_simple.hh

%build
scons DEBUG=yes RUBBERBAND=yes PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -dp -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/samples
install -m 644 samples/*.wav $RPM_BUILD_ROOT%{_datadir}/%{name}/samples

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING NEWS README doc/manual.html
%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.2
- Rebuilt for Fedora
* Wed Jul 15 2009 Fabian Affolter <fabian@bernewireless.net> - 0.12.0-1
- Updated to new upstream version 0.12.0
* Sun Apr 19 2009 Fabian Affolter <fabian@bernewireless.net> - 0.11.0-1
- Initial package for Fedora
