Name:           xlogo-lang
Version:        0.9.96pre
Release:        3.1
License:        GPL-2.0+
Summary:        Logo interpreter, written in Java
URL:            https://xlogo.tuxfamily.org/
Group:          Development/Tools/IDE
Source0:        xlogo-0.9.96pre-2012-06-27.tar.gz
Source1:        xlogo.desktop
Source2:        xlogo.png
BuildRequires:  ant
BuildRequires:  java-11-openjdk-devel lua
Requires:       java
BuildArch:      noarch

%description
Logo is a programming language developed in the 1970's by Seymour Papert. It
is an excellent language to begin learning with, as it teaches the basics of
things like loops, tests, procedures, etc. The user moves an object called a
"turtle" around the screen using commands as simple as forward, back, right,
and so on. As it moves, the turtle leaves a trail behind it, and so it is
therefore possible to create drawings. Operations on lists and words are also
possible.

%prep
%setup -q -n xlogo-0.9.96pre-2012-06-27
sed -i 's|1\.5|1.7|' build.xml

%build
%ant -DsignJar=false -DbuildSrc=false -Dplatform=linux deploy

%install
export NO_BRP_CHECK_BYTECODE_VERSION="true"
%{__install} -Dm755 deploy/xlogo.jar %{buildroot}%{_datadir}/%{name}/%{name}-%{version}.jar
# startscript
cat > %{name}.sh << EOF
#!/bin/sh
java -jar %{_datadir}/%{name}/%{name}-%{version}.jar
EOF
%{__install} -Dm755 %{name}.sh %{buildroot}%{_bindir}/%{name}
# Icon
%{__install} -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
# Desktop menu entry
%{__install} -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jun 08 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.96pre
- Rebuilt for Fedora
* Sun Dec 16 2012 lars@linux-schulserver.de
- fix license to be in SPDX format
- specfile cleanup
* Wed Aug  5 2009 lars@linux-schulserver.de
- add new ant properties
- set ant singJar property to false
- specfile cleanup
* Mon May 18 2009 kirill.kirillov@gmail.com
- Update to version 0.9.95
  + Manual has been rewritten
  + New primitives:
  * setdigits: Allow to set an arbitrary number of digits while calculating
  * decimales: Returns the number of digits precision while calculating
  * text: Returns all information on a procedure (variable, body)
  * externalcommand: Allow to launch an external command from XLogo
  * mp3play, mp3stop: Playing mp3
  + New language added: asturian,catalan,hungarian,italian
  + Modified primitives: define, zoom, setzoom
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Sun Jun  8 2008 kirill.kirillov@gmail.com
- Update to version 0.9.93
  + Better viewer 3d
  + Two new loop struture: primitives forever and foreach.
  + New language: greek
  + Better editor performance. Support for large files (several thousand lines).
  + Better workspace management
  + Two new arithmetic primitives: log, exp
  + Primitives ed, edall for editor
  + Ability to select a zone on the drawing area using the mouse
  + Primitive ifelse
- xlogo.jar is actually built from source codes
* Sun Mar 23 2008 kirill.kirillov@gmail.com
- Initial build of version 0.9.92 for openSUSE-Education
