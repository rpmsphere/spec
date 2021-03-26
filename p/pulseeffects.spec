%define oname PulseEffects

Summary:	Audio equalizer, filters and effects for Pulseaudio applications
Name:		pulseeffects
Version:	3.2.3
Release:	5.1
License:	GPLv3+
Group:		Sound
URL:		https://github.com/wwmm/pulseeffects
Source0:	https://github.com/wwmm/pulseeffects/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson >= 0.40.0
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gstreamer-1.0) >= 1.12
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0) >= 1.12
BuildRequires:	pkgconfig(gstreamer-insertbin-1.0) >= 1.12
BuildRequires:	pkgconfig(gstreamer-plugins-bad-1.0) >= 1.12
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(lilv-0) >= 0.22
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(py3cairo)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-numpy
BuildRequires:	python3-scipy
Requires:	python3-gi-cairo
Requires:	calf
Requires:	python3-gstreamer1.0
Requires:	python3-numpy
Requires:	python3-scipy
Requires:	gstreamer1-python >= 1.12
Requires:	gstreamer1-ladspa >= 1.12
Requires:	gstreamer1-lv2
Requires:	gstreamer1-plugins-good >= 1.12
Requires:	lv2
Requires:	rubberband
Requires:	typelib(GstInsertBin)
Requires:	typelib(GstBase)
# Maximizer plugin requires zam-plugins, we don't have it yet
BuildArch:	noarch

%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer and auto volume effects for PulseAudio applications.

%files -f %{oname}.lang
%doc CHANGELOG.md LICENSE.md README.md
%{_datadir}/metainfo/com.github.wwmm.pulseeffects.appdata.xml
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%dir %{python3_sitelib}/%{oname}
%dir %{python3_sitelib}/%{oname}Test
%{python3_sitelib}/%{oname}/*
%{python3_sitelib}/%{oname}Test/*

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

mv %{buildroot}%{_datadir}/applications/com.github.wwmm.pulseeffects.desktop \
   %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{oname}

%changelog
* Fri Jun 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.3
- Rebuild for Fedora
* Mon Jun 04 2018 vladi105 <vladi105@mail.ru> 3.2.3-2
- (3f6aeac) Merge pull request #3 from vladi105/pulseeffects:rosa2016.1
- (3f6aeac) add requires
