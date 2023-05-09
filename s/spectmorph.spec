Name:           spectmorph
Version:        0.5.2
Release:        1
Summary:        Analyze samples of musical instruments and combine them
Group:          Multimedia
License:        LGPLv3
URL:            http://spectmorph.org/
Source:         http://spectmorph.org/files/releases/%{name}-%{version}.tar.bz2
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
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/%{name}
%{_mandir}/man1/*.1.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
