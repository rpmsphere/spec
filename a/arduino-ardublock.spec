Name:		arduino-ardublock
Version:	20140828
Release:	1.bin
Summary:	Visual Programming Environment for Arduino
License:	GPLv3
Group:		Development/Education
Source0:	https://sourceforge.net/projects/ardublock/files/ardublock-beta-%{version}.jar
URL:		https://sourceforge.net/projects/ardublock/
Requires:	arduino
BuildArch:	noarch

%description
ArduBlock is a Block Programming Language for Arduino.
The language and functions model closely to Arduino Language Reference.

%prep
%setup -T -c

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -d $RPM_BUILD_ROOT%{_datadir}/arduino/tools/ArduBlockTool/tool
%__install -m644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/arduino/tools/ArduBlockTool/tool

%files
%{_datadir}/arduino/tools/ArduBlockTool

%changelog
* Thu Nov 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20140828
- Initial binary package
