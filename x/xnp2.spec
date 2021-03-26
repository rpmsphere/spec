Name:           xnp2
Version:        20120302
Release:        14.4
Summary:        NEC pc9801 computer emulator
Group:          System/Emulators/PC
License:        BSD
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/build-root-%{name}
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ libtool
BuildRequires:  gtk2-devel nasm
BuildRequires:  SDL-devel SDL_sound-devel SDL_mixer-devel
BuildRequires:  libXv-devel

%description
xnp2 is neko project II linux version.
neko project II is NEC pc9801 computer emulator.

%prep
%setup -q

%build
cd x11
%configure 
make %{?_smp_mflags}

%install
cd x11
make install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_mandir}/man1/xnp2.*
%{_bindir}/xnp2
%dir %{_datadir}/xnp2
%{_datadir}/xnp2/*

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20120302
- Rebuild for Fedora
* Wed Mar 07 2012 kobayashi 0.83
- Create package in openSUSE Build
