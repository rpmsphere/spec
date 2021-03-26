Name: abcmidi
Summary: ABC <-> Midi conversion utilities
Version: 2020.08.09
Release: 1
Group: Applications/Sound
License: GPL
URL: http://ifdo.ca/~seymour/runabc/top.html
Source: http://ifdo.ca/~seymour/runabc/abcMIDI-%{version}.zip

%description
The abcMIDI package contains four programs: abc2midi to convert ABC music
notation to midi, midi2abc to convert midi files to (a first approximation
to) the corresponding ABC, abc2abc to reformat and/or transpose ABC files,
and yaps to typeset ABC files as PostScript.

For a description of the abc syntax, please see the abc userguide which is a
part of the abc2mtex package written by Chris Walshaw.

%prep
%setup -q -n %{name}

%build
LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 abc2midi $RPM_BUILD_ROOT%{_bindir}
install -m 755 abcmatch $RPM_BUILD_ROOT%{_bindir}
install -m 755 midi2abc $RPM_BUILD_ROOT%{_bindir}
install -m 755 midicopy $RPM_BUILD_ROOT%{_bindir}
install -m 755 abc2abc $RPM_BUILD_ROOT%{_bindir}
install -m 755 mftext $RPM_BUILD_ROOT%{_bindir}
install -m 755 yaps $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/abc2abc.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/abc2midi.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/mftext.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/midi2abc.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/midicopy.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 doc/yaps.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc doc/ samples/ pt/ VERSION
%doc %{_mandir}/*
%{_bindir}/*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2020.08.09
- Rebuild for Fedora
