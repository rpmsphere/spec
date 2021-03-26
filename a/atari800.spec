Name:			atari800
Version:		4.0.0
Summary:		An emulator of 8-bit Atari personal computers
License:		GPLv2
URL:			https://atari800.github.io/
Source:			http://prdownloads.sourceforge.net/atari800/%{name}-%{version}.tar.gz
Group:			Console/Emulators
Release:		4.1
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	readline-devel
BuildRequires:	SDL-devel

%description
Atari800 is an emulator for the 800, 800XL, 130XE and 5200 models of
the Atari personal computer. It can be used on console, FrameBuffer or X11.
It features excellent compatibility, HIFI sound support, artifacting
emulation, precise cycle-exact ANTIC/GTIA emulation and more.

Authors:
David Firth
and Atari800 Development Team (see CREDITS for a full list)

%prep
%setup -q

%build
cd src
%configure --target=x11
%{__make} %{?jobs:-j%jobs}

%install
cd src
install -Dm 755 atari800 $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -Dm 644 %{name}.man $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%doc COPYING README.1ST DOC/*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed May 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.0
- Rebuild for Fedora
