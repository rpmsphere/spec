Name:           autojar
Version:        2.1
Release:        1
Summary:        Generating self-contained jars starting from a given list of classes
License:        GPL
Source0:	http://prdownloads.sourceforge.net/autojar/%{name}-%{version}.tar.gz
Source1:	%{name}
URL:            http://autojar.sourceforget.net/
Group:          Development/Java
BuildArch:      noarch
BuildRequires: java-devel-openjdk lua
BuildRequires: ant
BuildRequires: log4j
BuildRequires: ant-apache-log4j
BuildRequires: apache-log4j-extras
BuildRequires: bcel

%description 
AutoJar generates self-contained jars starting from a given list of classes.
It searches the bytecode recursively for referenced classes, extracts
the corresponding files from wherever they reside, and creates an archive
containing only the classes you really need.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
#sed -i 's|import org.apache.log4j|import org.apache.logging.log4j|' src/de/monoped/utils/FileExpand.java

%build
export CLASSPATH=%(build-classpath bcel)
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  -Dbcel.apiurl=%{_javadocdir}/bcel \
  jar javadoc

%install
rm -fr $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/usr/bin
install -d -m 755 $RPM_BUILD_ROOT/usr/share/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%files
%doc COPYING
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_bindir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_1jpp1.7
- converted from JPackage by jppimport script
* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp1.7
- converted from JPackage by jppimport script
