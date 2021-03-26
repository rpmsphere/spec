Name:		dsp-emulator
Summary:	DSP Emulator
Version:	0.14b2
Release:	12
URL:		https://code.google.com/p/dsp-emulator/
Source0:	https://dsp-emulator.googlecode.com/files/dsp_014b2_src.7z
Source1:	%{name}.desktop
Source2:	%{name}.png
License:	GPL-3.0
Group:		Games/Emulator
BuildRequires:	p7zip
BuildRequires:	lazarus
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel

%description
Delphi & Lazarus+Free Pascal free emulator. Arcade, Spectrum, Amstrad CPC,
NES, Coleco Vision...

%prep
%setup -q -n lazarus

%build
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=gtk2 \
	-B dsp.lpi

%install
install -D -m755 ../../%{name}_lazarus %buildroot%{_bindir}/%{name}
install -D -m644 %{SOURCE1} %buildroot%{_datadir}/applications/%{name}.desktop
install -D -m644 %{SOURCE2} %buildroot%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %buildroot

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jul 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14b2
- Rebuild for Fedora
