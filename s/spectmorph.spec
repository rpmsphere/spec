%undefine _debugsource_packages
%global __spec_install_post %{nil}

Name:           spectmorph
Version:        0.6.1
Release:        1
Summary:        Analyze samples of musical instruments and combine them
Group:          Multimedia
License:        LGPLv3
URL:            https://spectmorph.org/
Source:         https://spectmorph.org/files/releases/%{name}-%{version}.tar.bz2
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
%setup -q
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

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora
