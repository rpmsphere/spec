%global debug_package %{nil}

Name:		beye
Version:	6.1.0
Release:	7.1
Summary:	Console hex viewer/editor and disassembler
License:	GPLv2+
Group:		File tools
URL:		http://sourceforge.net/projects/beye/
Source:		biew-610.tar.bz2
Patch0:		biew610-fix-str-fmt.patch
Provides:   biew

%description
BEYE (Binary EYE) is a free, portable, advanced file viewer with built-in editor
for binary, hexadecimal and disassembler modes. It contains a highlight
AVR/Java/i86-AMD64/ARM-XScale/PPC-64 and other disassembler, full preview of
MZ,NE,PE,ELF and other.

%prep
%setup -q -n biew-610
%patch0 -p0

%build
CFLAGS=$RPM_OPT_FLAGS" -mmmx -msse"
CXXFLAGS=$RPM_OPT_FLASG" -mmmx -msse"
./configure --enable-curses --libdir=%{_libdir} --prefix=%_prefix
make TARGET_OS=linux USE_MOUSE=n PREFIX=%_prefix

%install
rm -rf %buildroot
install -d %buildroot{%{_bindir},%{_datadir}/%{name},%{_mandir}/man1}
install -m 755 biew %buildroot%{_bindir}/%{name}
cp -a bin_rc/{xlt,skn,*.hlp} %buildroot%{_datadir}/%{name}
install doc/biew.1 %buildroot%{_mandir}/man1/%{name}.1

%clean
rm -rf %buildroot

%files
%doc doc/*.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man?/%{name}.1*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 6.1.0
- Rebuild for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 6.1.0-3.mga3
+ Revision: 346901
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Jan 09 2013 boklm <boklm> 6.1.0-2.mga3
+ Revision: 343936
- remove unused macros
* Sun Jun 12 2011 kharec <kharec> 6.1.0-1.mga2
+ Revision: 104890
- imported package biew