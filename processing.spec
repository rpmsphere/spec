%define __os_install_post %{nil}

Name:		processing
Version:	3.0.2
Release:	1.bin
License:	GPL
Group:		Development/Java
URL:		http://processing.org/
Summary:	An open source programming language and environment
Source0:	http://download.processing.org/%{name}-%{version}-linux64.tgz
Source1:	http://download.processing.org/%{name}-%{version}-linux32.tgz
Source2:	processing.png
Requires:	java-devel-openjdk, unixODBC
Requires:	libCg
NoSource:	0
NoSource:	1

%description
Processing is an open source programming language and
environment for people who want to program images, animation,
and interactions. It is used by students, artists, designers,
researchers, and hobbyists for learning, prototyping, and production.
It is created to teach fundamentals of computer programming
within a visual context and to serve as a software sketchbook
and professional production tool. Processing is an alternative
to proprietary software tools in the same domain.

%prep
%ifarch x86_64
%setup -q -T -b 0
%else
%setup -q -T -b 1
%endif

%install
cd %{name}-%{version}
export NO_BRP_CHECK_BYTECODE_VERSION="true"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

%__mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd /usr/share/processing
./processing
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

#Icon
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

#Menu entry
install -d -m755 $RPM_BUILD_ROOT/%{_datadir}/applications
cat > $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Exec=%{name}
Icon=%{name}
Terminal=false
Name=Processing
Comment=%{summary}
Categories=Development; 
EOF

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Mar 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.2
- Rebuild binary package
