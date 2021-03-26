# set this to 1 if you want to build semistatic rpm
%define        semistatic      0
%{?_with_semistatic: %{expand: %%define semistatic 1}}
%{?_without_semistatic: %{expand: %%define semistatic 0}}

%define  rel     1
  
# default settings:  
%define BACKWARDCOMPATIBILITY ""  
%define UNICODE "--enable-unicode"  

Name: holtz
Version: 1.4.1
Release: %rel

Summary: Holtz is an implementation of the abstract board games Zertz and Dvonn
License: GPL
Group: Recreation/
Vendor: Martin Trautmann <martintrautmann@gmx.de>
URL: http://holtz.sourceforge.net/

Source: %name-%version.tar.gz

Prefix: %_prefix

## distribution specific settings

## SUSE
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1140
%if %{semistatic}
#I am not sure about precise requirements of wxGTK-static
Requires:      gtk+ >= 1.2.7 gettext
BuildRequires: wxWidgets >= 2.8.4 wxWidgets-devel gcc-c++ boost-devel
#wxGTK-static has to be manually compiled
%else
Requires:      wxWidgets >= 2.8.4
BuildRequires: wxWidgets-devel >= 2.8.4 gcc-c++ boost-devel
%endif
%else
%if %{semistatic}
#I am not sure about precise requirements of wxGTK-static
Requires:      gtk+ >= 1.2.7 gettext
BuildRequires: wxGTK >= 2.8.4 wxGTK-devel gcc-c++ boost-devel
#wxGTK-static has to be manually compiled
%else
Requires:      wxGTK >= 2.8.4
BuildRequires: wxGTK-devel >= 2.8.4 gcc-c++ boost-devel
%endif
%endif

## Fedora
%else
%if 0%{?fedora}
%if %{semistatic}
#I am not sure about precise requirements of wxGTK-static
Requires:      gtk+ >= 1.2.7 gettext
BuildRequires: wxGTK >= 2.8.4 wxGTK-devel gcc-c++ boost-devel
#wxGTK-static has to be manually compiled
%else
Requires:      wxGTK >= 2.8.4
BuildRequires: wxGTK-devel >= 2.8.4 gcc-c++ boost-devel
%endif

## Mandriva
%else
%if 0%{?mdkversion}
#%if 0%{?mdkversion} < 201100
%define UNICODE "--disable-unicode"
#%endif  
%if %{semistatic}
#I am not sure about precise requirements of wxGTK-static
Requires:      gtk+ >= 1.2.7 gettext
BuildRequires: wxGTK >= 2.8.4 wxGTK-devel gcc-c++ boost-devel
#wxGTK-static has to be manually compiled
%else
Requires:      wxGTK >= 2.8.4
BuildRequires: wxGTK-devel >= 2.8.4 gcc-c++ boost-devel
%endif

## Redhat / Centos
%else
%if 0%{?rhel_version} || 0%{?centos_version}
%if %{semistatic}
#I am not sure about precise requirements of wxGTK-static
Requires:      gtk+ >= 1.2.7 gettext
BuildRequires: wxGTK >= 2.8.4 wxGTK-devel gcc-c++ boost-devel
#wxGTK-static has to be manually compiled
%else
Requires:      wxGTK >= 2.8.4
BuildRequires: wxGTK-devel >= 2.8.4 gcc-c++ boost-devel
%endif

## any other (just speculation what might be most common)
%else
%if %{semistatic}
#I am not sure about precise requirements of wxGTK-static
Requires:      gtk+ >= 1.2.7 gettext
BuildRequires: wxGTK >= 2.8.4 wxGTK-devel gcc-c++ boost-devel
#wxGTK-static has to be manually compiled
%else
Requires:      wxGTK >= 2.8.4
BuildRequires: wxGTK-devel >= 2.8.4 gcc-c++ boost-devel
%endif
# if Redhat else any other
%endif 
# if Mandriva else Redhat+
%endif
# if Fedora else Mandriva+
%endif
# if Suse else Fedora+
%endif


%description
Holtz is an implementation of the two player abstract board games Zertz and Dvonn from the gipf probject (www.gipf.com).
Zertz is about placing and collecting stones, making sacrifices, and a continuously shriking board. 
Dvonn is about controlling stacks of stones which can jump on other stacks to capture them and keeping 
contact to the three dvonn stones. Version 1.3.0 added a third game called Relax which resembles the game
"Take it Easy"

%prep
%setup -q
#perl -pi -e 's|\${prefix}|%prefix|' README
#perl -pi -e 's|PREFIX|%prefix|' doc/FAQ

%build

if [ ! -x configure ]; then
	CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $ARCH_FLAGS --prefix=%prefix
fi
%if %{semistatic}
	CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --enable-wxstatic %BACKWARDCOMPATIBILITY %UNICODE $ARCH_FLAGS --prefix=%prefix
%else
	CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --disable-wxstatic %BACKWARDCOMPATIBILITY %UNICODE $ARCH_FLAGS --prefix=%prefix
%endif

if [ -n "$SMP" ]; then
	make -j$SMP "MAKE=make -j$SMP"
else
	make
fi

%install
rm -rf $RPM_BUILD_ROOT
#mkdir -p -m 755 $RPM_BUILD_ROOT%prefix/{{include,lib}/%lib_name}
make install-strip prefix=$RPM_BUILD_ROOT%prefix

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README NEWS ChangeLog TODO Rules.german Rules.english
%prefix/bin/*
%prefix/share/locale/*/LC_MESSAGES/*.mo
%prefix/share/holtz/skins/*
%prefix/share/holtz/sounds/*
%prefix/share/holtz/help/*
%prefix/share/holtz/

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuild for Fedora
* Fri May 18 2012 alantom<alan@ossii.com.tw>
- rebuild for OX
* Fri May 27 2011 version Martin Trautmann <martintrautmann@gmx.de>
- added support for OpenSuSE >= 11.4
- added support for Fedora 14/15
- added support for Mandriva
- CentOS 5, RHEL 5 and possibly RHEL 6 have no wxGTK 2.8 packages (I didn't find any)
- CentOS 6 is not available in build service, yet
