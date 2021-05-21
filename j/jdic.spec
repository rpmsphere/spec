Name:		jdic
Version:	0.9.4
Release:	1
Summary:	The JDesktop Integration Components (JDIC)
URL:		https://jdic.dev.java.net/
Group:		Development/Java
License:	LGPLv2+
Source:		jdic-%{version}-src.zip
Patch0:		jdic-disable_jnlp.patch
Patch1:		jdic-WebBrowserUtil_fixbuild.patch
Patch2:		jdic-mozilla_makefile.patch
Patch3:		jdic-mozembed.patch
Patch4:		jdic-build_libdir.patch
Patch5:		jdic-jni_makefile.patch
BuildRequires:	ant libgnome-devel xulrunner-devel nspr-devel
BuildRequires:	gtk2-devel
Requires:	java >= 1.6.0

%description
The JDesktop Integration Components (JDIC) project aims to make Java™
technology-based applications ("Java applications") first-class citizens
of current desktop platforms without sacrificing platform independence.
Its mission is to enable seamless desktop/Java integration.

JDIC provides Java applications with access to functionalities and
facilities provided by the native desktop. It consists of a collection
of Java packages and tools.

%package javadoc
Summary:	Javadoc for JDIC
Group:		Development/Java
%description javadoc
Javadoc for JDIC

%prep
%setup -q -n jdic-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
sed -i 's|<property name="usr.lib.dir".*|<property name="usr.lib.dir" value="%{_libdir}" />|' jdic/build.xml
sed -i 's|toolkit instanceof sun.awt.motif.MToolkit|false|' jdic/src/unix/classes/org/jdesktop/jdic/tray/internal/impl/GnomeTrayAppletService.java

%build
cd jdic
%ant buildall

%install
%{__rm} -Rf %{buildroot}
cd jdic/dist/linux
%{__mkdir_p} %{buildroot}%{_javadir} %{buildroot}%{_libdir} %{buildroot}%{_bindir}
%{__install} %{name}.jar %{buildroot}%{_javadir}
%{__install} lib%{name}.so %{buildroot}%{_libdir}
%{__install} libtray.so %{buildroot}%{_libdir}
%{__install} libmozembed-linux-gtk2.so %{buildroot}%{_libdir}
%{__install} mozembed-linux-gtk2 %{buildroot}%{_bindir}

%files
%doc COPYING README.html
%{_javadir}/%{name}.jar
%{_libdir}/lib%{name}.so
%{_libdir}/libtray.so
%{_libdir}/libmozembed-linux-gtk2.so
%{_bindir}/mozembed-linux-gtk2

%files javadoc
%doc jdic/dist/linux/javadoc
%doc jdic/dist/linux/demo

%changelog
* Mon Dec 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuilt for Fedora
* Tue May 13 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.9.4-0.0.1mdv2009.0
+ Revision: 206742
- new version
- fix build for openjdk
  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix no-buildroot-tag
* Wed Sep 19 2007 Nicolas Vigier <nvigier@mandriva.com> 0.9.3-2mdv2008.0
+ Revision: 90609
- rebuild
- Import jdic
