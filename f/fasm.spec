%global no_install_post_strip 1
%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

Summary:        Flat assembler
Summary(pl):    "Płaski" assembler
Name:           fasm
Version:        1.73.32
Release:        1
License:        distributable
Group:          Development/Tools
Source0:        https://flatassembler.net/%{name}-%{version}.tgz
URL:            https://flatassembler.net/

%description
The flat assembler is a fast and efficient self-assembling 80x86
assembler for DOS, Windows and Linux operating systems. Currently it
supports all 8086-80486/Pentium instructions with MMX, SSE, SSE2, SSE3
and 3DNow! extensions, can produce output in binary, MZ, PE, COFF or
ELF format. It includes the powerful but easy to use macroinstruction
support and does multiple passes to optimize the instruction codes for
size. The flat assembler is self-compilable and the full source code
is included.

%description -l pl
Płaskie Assembler jest szybkie i efektywne samoskładających 80x86
asembler dla systemów operacyjnych DOS, Windows i Linux. obecnie
obsługuje wszystkie instrukcje 8086-80486 / Pentium MMX, SSE, SSE2, SSE3
i 3DNow! Rozszerzenia, może produkować wyjście w formacie binarnym, MZ, PE, lub COFF
Format ELF. Obejmuje on potężny, ale łatwy w użyciu makroinstrukcję
Wsparcie i robi wiele podań do optymalizacji kodu Instrukcją
rozmiar. Płaska monter jest self-compilable oraz pełny kod źródłowy
jest włączone.

%prep
%setup -q -n %{name}

%build
cd source/Linux/x64
../../../%{name}.x64 %{name}.asm

%install
install -Dm755 source/Linux/x64/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc *.txt
%{_bindir}/*

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.73.32
- Rebuilt for Fedora
* Sun Aug 29 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.3  2004/08/29 15:17:22  undefine
- update to 1.55
Revision 1.2  2004/08/05 20:02:48  qboosh
- bcond header, pl cosmetics
Revision 1.1  2004/08/05 18:04:26  undefine
- initital rpm version
