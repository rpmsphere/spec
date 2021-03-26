%define debug_package	%{nil}

Name:		java3d
Version:	1.5.2
Release:	15
Summary:	The Java 3D API
Group:		Development/Java
License:	BSD, GPL
URL:		https://java3d.java.net/
# svn export https://svn.java.net/svn/j3d-core~svn/tags/rel-1_5_2-fcs j3d-core-1.5.2
# tar czf j3d-core-1.5.2-src-svn.tar.gz j3d-core
Source0:	j3d-core-%{version}-src-svn.tar.gz
# http://java.net/projects/j3d-core-utils
# svn export https://svn.java.net/svn/j3d-core-utils~svn/tags/rel-1_5_2-fcs j3d-core-utils
# tar czf j3d-core-utils-1.5.2-src-svn.tar.gz j3d-core-utils
Source1:	j3d-core-utils-%{version}-src-svn.tar.gz
# svn export https://svn.java.net/svn/j3d-optional-utils~svn/tags/rel-1_5_2-fcs j3d-optional-utils
# tar czf j3d-optional-utils-1.5.2-src-svn.tar.gz j3d-optional-utils
Source4:	j3d-optional-utils-%{version}-src-svn.tar.gz
# svn export https://svn.java.net/svn/j3d-examples~svn/tags/rel-1_5_2-fcs j3d-examples
# tar czf j3d-examples-1.5.2-src-svn.tar.gz j3d-examples
Source5:	j3d-examples-%{version}-src-svn.tar.gz
Patch0:		01_fix_powerpc_ftbfs.patch
Patch1:		02_fix_generic_ftbfs.patch
Patch2:		03_fix_ia64_ftbfs.patch
Patch3:		04_no_maxmemory.patch
Patch4:		05_pic_amd64.patch
Patch5:		05_pic_i586.patch
Patch6:		06_java-compat.patch
Patch7:		typedef.patch

BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	glibc-devel
BuildRequires:	java-devel
%ifnarch %{arm} aarch64
BuildRequires:	jogl2
%endif
BuildRequires:	javapackages-local
BuildRequires:	junit
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)
BuildRequires:	vecmath
BuildRequires:	xerces-j2
BuildRequires:	xml-commons-apis

Requires:	java
Requires:	javapackages-tools

Provides:	j3dcore == %{version}
Provides:	j3dutils == %{version}

%description
The Java 3D API provides a set of object-oriented interfaces that
support a simple, high-level programming model you can use to
build, render, and control the behavior of 3D objects and visual
environments. With the Java 3D API, you can incorporate high quality,
scalable, platform-independent 3D graphics into applications andvecmath
applets based on Java technology.

#-------------------------------------------------------------------------

%package	examples
# http://java.net/projects/j3d-examples
Summary:	Java 3D Example Programs
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	javapackages-tools

%description examples
The Java 3D API.

This package contains Java 3D Example Programs.

#-------------------------------------------------------------------------

%package	optional-utils
# http://java.net/projects/j3d-optional-utils
Summary:	Java 3D Optional Utilities
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	javapackages-tools

%description optional-utils
The Java 3D API.

This package contains Java 3D Optional Utilities.

#-------------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	javapackages-tools

%description javadoc
The Java 3D API.

This package contains javadoc for %{name}

#-------------------------------------------------------------------------

%prep
%setup -q -T -c -n %{name}-%{version}
# core
tar xf %{SOURCE0}
# core-utils
tar xf %{SOURCE1}
# optional-utils
#tar xf %%{SOURCE4}
# examples
tar xf %{SOURCE5}

%autopatch -p1

for j in $(find . -name "*.jar"); do
  mv $j $j.no
done

for c in $(find . -name "*.class"); do
  rm -f $c
done

%build
export ANT_OPTS=-Xmx256m
export CLASSPATH=$PWD/j3d-core/build/default/opt/lib/ext/j3dcore.jar:junit.jar:%{_datadir}/java/vecmath.jar

pushd j3d-core
	%ant \
	-Dant.javadoc.maxmemory=512m \
	-Dbuild.type=stable \
	jar-opt docs-public
popd

# TODO require JOAL http://java.net/projects/joal/ and OpenAL
#pushd j3d-optional-utils
#	%%ant dist
#popd

CLASSPATH=$CLASSPATH:$PWD/j3d-core/build/default/opt/lib/ext/j3dutils.jar
pushd j3d-examples
	%ant all
popd


%install
mkdir -p %{buildroot}%{_javadir}/%{name}
mkdir -p %{buildroot}%{_libdir}

install -m 644 j3d-core/build/default/opt/lib/ext/j3dcore.jar \
    %{buildroot}%{_javadir}/%{name}/j3dcore-%{version}.jar
install -m 644 j3d-core/build/default/opt/lib/ext/j3dutils.jar \
    %{buildroot}%{_javadir}/%{name}/j3dutils-%{version}.jar
#install -m 644 j3d-optional-utils/joalmixer/build/lib/ext/joalmixer.jar\
#    %%{buildroot}%%{_javadir}/java3d/
install -m 644 j3d-examples/dist/j3d-examples.jar \
    %{buildroot}%{_javadir}/%{name}/

(
  cd %{buildroot}%{_javadir}/%{name}
  for jar in *-%{version}*; do
    ln -sf ${jar} ${jar/-%{version}/}
  done
)

# TODO build libj3dcore-ogl-cg.so require NVDIA CG Toolkit
install -m 755 j3d-core/build/default/opt/native/libj3dcore-ogl.so \
    %{buildroot}%{_libdir}/libj3dcore-ogl.so

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -a j3d-core/build/*/javadocs/docs-public/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc j3d-core/*.txt j3d-core/*.html j3d-core/docs
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/j3dcore-%{version}.jar
%{_javadir}/%{name}/j3dcore.jar
%{_javadir}/%{name}/j3dutils-%{version}.jar
%{_javadir}/%{name}/j3dutils.jar
%{_libdir}/libj3dcore-ogl.so

%files examples
%doc j3d-examples/*.txt j3d-examples/*.html
%{_javadir}/%{name}/j3d-examples.jar

#%%files optional-utils
#%%doc j3d-optional-utils/*.txt j3d-optional-utils/joalmixer/README.txt
#%%{_javadir}/%%{name}/joalmixer.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri May 17 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.2
- Rebuild for Fedora
* Tue Oct 09 2018 pterjan <pterjan> 1.5.2-15.mga7
+ Revision: 1318860
- Also do not require jogl on aarch64
* Sun Sep 23 2018 umeabot <umeabot> 1.5.2-14.mga7
+ Revision: 1298352
- Mageia 7 Mass Rebuild
* Fri Sep 29 2017 daviddavid <daviddavid> 1.5.2-13.mga7
+ Revision: 1161671
- disable debug package
* Mon Oct 03 2016 pterjan <pterjan> 1.5.2-12.mga6
+ Revision: 1058174
- Do not require jogl on arm (not sure if it is needed elsewhere)
* Sat Feb 27 2016 umeabot <umeabot> 1.5.2-11.mga6
+ Revision: 979918
- Mageia 6 Mass Rebuild
* Sat Feb 07 2015 pterjan <pterjan> 1.5.2-9.mga5
+ Revision: 814007
- Sync with Debian to fix build
+ umeabot <umeabot>
- Second Mageia 5 Mass Rebuild
- Mageia 5 Mass Rebuild
+ david-david <david-david>
- update URL
* Tue Oct 22 2013 umeabot <umeabot> 1.5.2-6.mga4
+ Revision: 541515
- Mageia 4 Mass Rebuild
* Sun Oct 13 2013 joequant <joequant> 1.5.2-5.mga4
+ Revision: 496108
- add vecmath buildrequires
- restore java3d and java3ds. Build against new vecmath
+ dmorgan <dmorgan>
- Package is retired, does not build against current java stack
* Tue Jul 30 2013 joequant <joequant> 1.5.2-4.mga4
+ Revision: 461159
- remove java-nodeps from buildrequires
* Mon Feb 18 2013 dmorgan <dmorgan> 1.5.2-3.mga3
+ Revision: 399020
- Add debian patches to fix build with java7
+ umeabot <umeabot>
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Nov 16 2011 dmorgan <dmorgan> 1.5.2-2.mga2
+ Revision: 168044
- Remove dupplicate %%changelog entry ( mga #3356)
- Fix group
- Add Buildrequire for native build
- Fix buildrequires
- Fix typo in classpath
- Try to fix build
- Remove unused rpm macros
- Cleaning in find
- More CLASSPATH fixes
- try to clean CLASSPATH
- Fix buildRequires
- Fix CLASSPATH ( from gil)
- Fix buildrequires
- Remove double %%prep
- Fix buildrequires
+ gil <gil>
- added new sub package examples
- imported package java3d
