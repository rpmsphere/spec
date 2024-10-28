%define _name   jMemorize

Name:           jmemorize
Summary:        Vocabulary learning program based on Leitner flashcard system
Summary(zh_TW): 利用 Leitner flashcard 製作的字彙學習程式
Group:          Amusements/Teaching/Language
Version:        1.3.1
Release:        1
License:        GPL
URL:            https://jmemorize.org
BuildArch:      noarch 
Requires:       java
BuildRequires:  unzip
BuildRequires:  chkconfig
BuildRequires:  java-devel-openjdk
BuildRequires:  ant
BuildRequires:  desktop-file-utils
Source0:        %{_name}-1.3.1-source.zip
Source1:        %{_name}.desktop
Source2:        %{_name}.png

%description
jMemorize is written in Java and uses Leitner-flashcards to make
memorizing facts not only more efficient but also more fun.
jMemorize manages your learn progress and features categories,
statistics and a visually appealing and intuitive interface.

Author(s):
------------
    Riad Djemili <jmemorize @ riad.de>

%prep
%setup -q -n %{_name}-%{version}
sed -i 's|="5"|="7"|g' build.xml

%build
%ant dist-bin

%install
%__install -d -m 755 %{buildroot}%{_javadir}/%{_name}
%__install -m 755 dist/%{version}/%{_name}-%{version}.jar %{buildroot}%{_javadir}/%{_name}/
# startscript
%__cat > %{_name} << EOF
#!/bin/sh
java -jar %{_javadir}/%{_name}/%{_name}-%{version}.jar
EOF
%__install -d -m 755 %{buildroot}%{_bindir}
%__install -m 755 %{_name} %{buildroot}%{_bindir}/
# Icon
%__install -D -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{_name}.png
# Desktop menu entry
%__install -d -m 755 %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{_name}.desktop

%files
%doc README LICENSE CHANGELOG 
%{_bindir}/*
%dir %{_javadir}/%{_name}
%{_javadir}/%{_name}/*
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/pixmaps/%{_name}.png

%changelog
* Fri Mar 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuilt for Fedora
* Fri Aug 27 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> -1.31-2.48.ossii
- add %%dist
* Tue Aug 24 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw>
- fix the name of src.rpm
* Fri Aug 13 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw>
- Rebuild rpm for OX
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Sun May 18 2008 lars@linux-schulserver.de
- fix default installation path for java packages
  (os-edu #0000046)
* Tue May  6 2008 lars@linux-schulserver.de
- beautify specfile
- own the datadir
* Thu May  1 2008 lumnis@email.de
- initial rpm build for jMemorize 1.3.1
