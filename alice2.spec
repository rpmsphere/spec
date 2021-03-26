%define __os_install_post %{nil}
%define debug_package %{nil}
%define _name Alice2

Name:		alice2
Version:	2.4.3
Release:	1.bin
Summary:	Innovative 3D programming environment
License:	Open Source <http://alice.org/index.php?page=license>
Group:		Applications/Development
Source0:	http://www.alice.org/downloads/2.4/Alice2_4e.tar.gz
Source1:	%{name}.png
URL:		http://alice.org/
AutoReqProv: off
Requires:	java-devel-openjdk
Requires:	libCg
NoSource:	0

%description
Alice is an innovative 3D programming environment that makes it easy to create
an animation for telling a story, playing an interactive game, or a video to
share on the web. Alice is a freely available teaching tool designed to be a
student's first exposure to object-oriented programming. It allows students to
learn fundamental programming concepts in the context of creating animated
movies and simple video games. In Alice, 3-D objects (e.g., people, animals,
and vehicles) populate a virtual world and students create a program to
animate the objects.

%prep
%setup -q -n "Alice 2.4"/Required
%ifarch x86_64
  rm -rf lib/linux-i586/*.so
%else
  rm -rf lib/linux-i586/amd64
%endif

%build

%install
%__mkdir_p %{buildroot}%{_libdir}/%{name}
%__cp -a * %{buildroot}%{_libdir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script

JAVA_HOME=/usr/lib/jvm/java
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
PATH=/usr/lib/jvm/java/bin:\$PATH

cd %{_libdir}/%{name}
./run-alice
EOF

# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{_name}
Comment=Innovative 3D programming environment
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;Java;
EOF

sed -i '1s|/usr/local|/usr|' %{buildroot}%{_libdir}/%{name}/jython-2.1/Lib/cgi.py

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Mar 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.3
- Initial binary package
