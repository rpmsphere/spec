Name:           derby
Version:        10.13.1.1
Release:        6.657
Summary:        Embeddable Database Engine Written in Java
License:        Apache-2.0
Group:          Productivity/Databases/Servers
URL:            https://db.apache.org/derby/
Source0:        https://www.apache.org/dist/db/derby/db-derby-%{version}/db-derby-%{version}-src.tar.gz
Source1:        %{name}.service
Source2:        %{name}-script
# https://issues.apache.org/jira/browse/DERBY-5125
Patch1:         derby-javacc5.patch
# For compatibility with lucene >= 4.10
Patch2:         derby-lucene.patch
Patch3:         derby-taglet.patch
Patch4:         derby-sourcetarget.patch
Patch5:         derby-javadoc-encoding.patch
Patch6:         derby-javacc7.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  jakarta-oro
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-tools
BuildRequires:  junit
#BuildRequires:  lucene
BuildRequires:  systemd
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis
Requires:       jakarta-oro
Requires:       java >= 1.8
Requires:       javapackages-tools
Requires:       xalan-j2
Requires:       xml-commons-apis
BuildArch:      noarch
%systemd_requires

%description
The Derby project develops open source database technology that is:

- Pure Java
- Easy to use
- Small footprint
- Standards based
- Secure

%package javadoc
Summary:        Embeddable Database Engine Written in Java
Group:          Development/Libraries/Java

%description javadoc
Javadoc generated documentation for derby database engine.

%prep
%setup -q -n db-derby-%{version}-src
find -name '*.jar' -delete
find -name '*.class' -delete

rm java/engine/org/apache/derby/impl/sql/compile/Token.java
rm java/build/org/apache/derbyBuild/javadoc/*.java
%patch 1
%patch 2
%patch 3
%patch 4 -p1
%patch 5 -p1
%patch 6

# Don't use Class-Path in manifests
sed -i -e '/Class-Path/d' build.xml

# Don't download online packagelists
sed -e 's/initjars,set-doclint,install_packagelists/initjars,set-doclint/' \
    -e '/<link offline/,+1d' \
    -i build.xml

dos2unix LICENSE NOTICE README

%build
# tools/ant/properties/extrapath.properties
ln -sf $(build-classpath javacc) tools/java/javacc.jar
ln -sf $(build-classpath glassfish-servlet-api) \
  tools/java/geronimo-spec-servlet-2.4-rc4.jar
ln -sf $(build-classpath xalan-j2) tools/java/xalan.jar
ln -sf $(build-classpath xalan-j2-serializer) tools/java/serializer.jar
ln -sf $(build-classpath oro) tools/java/jakarta-oro-2.0.8.jar
ln -sf $(build-classpath junit) tools/java/junit.jar
ln -sf $(build-classpath lucene/lucene-core) tools/java/lucene-core.jar
ln -sf $(build-classpath lucene/lucene-analyzers) tools/java/lucene-analyzers-common.jar
ln -sf $(build-classpath lucene/xml-query-parser) tools/java/lucene-queryparser.jar

# So that the build doesn't fail on a stack overflow
export ANT_OPTS="-Xss2m"

export CLASSPATH="$(build-classpath xml-commons-apis)"
ant \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    buildsource buildjars javadoc

%install
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}

# Systemd unit
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sbindir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
ln -s service %{buildroot}%{_sbindir}/rc%{name}

# Derby home dir
install -dm 755 %{buildroot}%{_localstatedir}/lib/derby

# Library
install -d %{buildroot}%{_javadir}/%{name}
for i in jars/sane/*.jar ; do
    B=$(basename $i |sed 's/.jar$//')
    install -m644 $i %{buildroot}%{_javadir}/%{name}/$B.jar
done

# Wrapper scripts
install -d %{buildroot}%{_bindir}
install -p -m755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-ij
for P in sysinfo NetworkServerControl startNetworkServer stopNetworkServer ; do
    ln %{buildroot}%{_bindir}/%{name}-ij %{buildroot}%{_bindir}/%{name}-$P
done

%fdupes %{buildroot}

%pre
getent group derby >/dev/null || groupadd -r derby
getent passwd derby >/dev/null || \
useradd -r -g derby -d %{_localstatedir}/lib/derby -s /sbin/nologin \
    -c "Apache Derby service account" derby
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE NOTICE
%doc README RELEASE-NOTES.html
%{_javadir}/%{name}
%{_bindir}/derby-NetworkServerControl
%{_bindir}/derby-ij
%{_bindir}/derby-startNetworkServer
%{_bindir}/derby-stopNetworkServer
%{_bindir}/derby-sysinfo
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%files javadoc
%license LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Sun May 29 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 10.13.1.1
* Wed Feb  6 2019 Fridrich Strba <fstrba@suse.com>
- Build against glassfish-servlet-api instead of servlet3
- Added patches:
  * derby-javadoc-encoding.patch
    + specify UTF-8 encoding to fix javadoc generation
  * derby-javacc7.patch
    + Fix build with JavaCC 7
* Fri Dec  7 2018 Fridrich Strba <fstrba@suse.com>
- Build against xml-commons-apis instead of xerces-j2-xml-apis
* Wed May 16 2018 fstrba@suse.com
- Added patch:
  * derby-sourcetarget.patch
    + Build all derby, even the derbyPreBuild, with source and
    target level 1.8
* Fri Dec 22 2017 fstrba@suse.com
- Don't build custom taglets, that are based on removed APIs
- Added patch:
  * derby-taglet.patch
    + Don't use custom taglets.
* Wed Sep 20 2017 fstrba@suse.com
- Version bump to 10.13.1.1
  * amongst others support for building with jdk9
  * require jdk8 or higher for build and on runtime
- Modified patch:
  * derby-lucene.patch
    + filter out targets that make no sense unless you are a
    maintainer
    + don't include Class-Path in jar files
* Mon Jun 20 2016 pjanouch@suse.de
- Give javac more stack space for the build, so that it doesn't
  fail pseudo-randomly (bsc#985388)
* Wed Jul 29 2015 tchvatal@suse.com
- Version bump to 10.11.1.1 bsc#1002763 CVE-2015-1832:
  * No upstream changelog visible
- Apply patches taken from fedora:
  * derby-lucene.patch
  * derby-javacc5.patch
* Wed Jul 29 2015 tchvatal@suse.com
- Previous change still didnt fix i386 build -> revert
* Tue Jul 28 2015 tchvatal@suse.com
- Add constraints on memory to ensure build always succeeds
* Thu Jul 17 2014 tchvatal@suse.com
- Version bump to latest and build from source.
* Tue Jul  8 2014 tchvatal@suse.com
- Cleanup with spec-cleaner.
* Mon Sep  9 2013 tchvatal@suse.com
- Move from jpackage-utils to javapackage-tools
* Tue Aug 14 2007 kejohnson@suse.de
- updated to 10.3.1.4 to fix several security bugs
  CVE-2005-4849, CVE-2006-7216, CVE-2006-7217 [291035]
- changed requires to JAVA 1.5 or greater
* Wed May  2 2007 dbornkessel@suse.de
- added unzip to BuildRequires
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Feb 21 2005 skh@suse.de
- initial package
