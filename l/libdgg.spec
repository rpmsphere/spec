Name:		libdgg
Version:	20170121
Release:	1
Summary:	Dynamically generates Han glyphs
License:	New BSD License
Group:		System/Libraries
Source0:	%{name}.zip
Source1:	%{name}.png
URL:		https://code.google.com/p/libdgg/
BuildRequires:	java-devel
BuildRequires:	ant
Requires:	jre
BuildArch:	noarch

%description
It's a JAVA cross platform library also a font engine which dynamically
generates Han glyphs by assembling Han components, and the meta data
inside Han glyphs can also be searched. By the software, lacking Han font
is no more.

It's simple. Just 2 things. Generating and searching.

%prep
%setup -q -n %{name}
sed -i -e 's|"檔"|"檔案"|' -e 's|"離"|"離開"|' -e 's|"助"|"求助"|' src/demo/Demo.java

%build
%ant dist

%install
%__install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a dist/* %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# libdgg script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS libdgg.jar
EOF

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=libdgg
Name[zh_TW]=動態組字示範
Comment=Demo for unicode Ideographic Description Sequence
Comment[zh_TW]=萬國碼表意文字描述序列演示
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Utility;Java;
EOF

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon May 08 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 20170121
- Initial package
