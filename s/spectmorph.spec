%undefine _debugsource_packages
%global __spec_install_post %{nil}

Name:           spectmorph
Version:        1.0.0
Release:        0.beta2
Summary:        Analyze samples of musical instruments and combine them
Group:          Multimedia
License:        LGPLv3
URL:            https://spectmorph.org/
Source:         https://spectmorph.org/files/releases/%{name}-%{version}-beta2.tar.bz2
BuildRequires:  qt5-qtbase-devel
BuildRequires:  cairo-devel
BuildRequires:  fftw-devel
BuildRequires:  libao-devel
BuildRequires:  libsndfile-devel

%description
SpectMorph can be used to construct hybrid sounds, for instance a sound between
a trumpet and a flute; or smooth transitions, for instance a sound that starts
as a trumpet and then gradually changes to a flute.

%prep
%setup -q -n %{name}-%{version}-beta2
%ifarch aarch64
sed -i 's|__m128|__int128|' lib/smnoisedecoder.cc
%endif

%build
%configure
make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_includedir}/%{name}
%exclude %{_libdir}/libspectmorph*.*a
%{_libdir}/libspectmorph*.so*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/vst/*.so
%{_libdir}/clap/SpectMorph.clap
%{_libdir}/lv2/spectmorph.lv2
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

%changelog
* Sun Dec 22 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0-0.beta2
- Rebuilt for Fedora
