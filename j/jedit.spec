Summary: Programmer's text editor written in Java
Name: jedit
Version: 4.3.3
#Version: 5.1.0
Release: 21.1
License: GPL
Group: Applications/Editors
URL: http://www.jedit.org/
Source0: http://dl.sf.net/jedit/%{name}%{version}source.tar.bz2
BuildArch: noarch
BuildRequires: ant
#BuildRequires: apache-ivy
BuildRequires: docbook-style-xsl
BuildRequires: java-devel-openjdk lua
BuildRequires: libxslt

%description
jEdit is an Open Source, cross platform text editor written in Java. It
has an extensive feature set that includes syntax highlighting, auto indent,
folding, word wrap, abbreviation expansion, multiple clipboards, powerful
search and replace, and much more.

Futhermore, jEdit is extremely customizable, and extensible, using either
macros written in the BeanShell scripting language, or plugins written
in Java.

%package javadoc
Summary: Javadoc for jEdit
Group: Development/Java   

%description javadoc
Javadoc for jEdit.

%prep
%setup -q -n jEdit
sed -i 's|compress="false"|compress="true"|' build.xml
sed -i 's|value="1.5"|value="1.7"|' build.xml
sed -i '/Cygwin detection/i \
	<property name="config.docbook.xsl" \
			  value="/usr/share/sgml/docbook/xsl-stylesheets" /> \
	<property name="config.docbook.catalog" \
			  value="/etc/sgml/xml-docbook-4.4.cat" /> \
	<property name="config.xsltproc.executable" \
			  value="/usr/bin/xsltproc" />' build.xml
sed -i 's|stop(new Abort());|new Abort();stop();|' org/gjt/sp/util/WorkThread.java

%build
%ant build

%install
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
# some cleanin'
rm -rf build/classes
# install
cp -r build/* $RPM_BUILD_ROOT%{_datadir}/%{name}

# script
%__install -dm 755 $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
java -jar %{_datadir}/%{name}/jedit.jar \$@
EOF
   
# script server
cat > $RPM_BUILD_ROOT%{_bindir}/%{name}-server <<EOF
#!/bin/sh
jedit -nogui -background
EOF

# icons
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__install -m 644 icons/%{name}-icon48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

# desktopfile
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=jEdit
Comment=Programmer's text editor written in Java
Exec=%{name} %U
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;TextEditor;
EOF
   
# manpage
%__install -dm 755 $RPM_BUILD_ROOT%{_mandir}/man1
%__install -m 644 package-files/linux/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop 

%changelog
* Thu Jun 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3.3
- Rebuilt for Fedora
* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 4.2-2 - 6256+/dag
- Fix typo in wrapper script.
* Wed Apr 09 2008 Dag Wieers <dag@wieers.com> - 4.2-1
- Initial package. (using DAR)
