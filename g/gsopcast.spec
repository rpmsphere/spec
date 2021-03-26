Name:           gsopcast
Requires:	    alsa wget tar
#Requires:      sopcast
BuildRequires:	gcc gcc-c++ libgnome-devel alsa-lib-devel pkgconfig perl-XML-Parser
URL:		    http://code.google.com/p/gsopcast/
# SVN repository:
# svn checkout http://gsopcast.googlecode.com/svn/trunk/ gsopcast-read-only
License:	    GNU General Public License (GPL)
Group:		    Productivity/Multimedia/Video/P2P
Version:	    0.4.0
Release:	    31.4
Summary:	    A GTK GUI front-end of sopcast
Source:         %name-%version.tar.bz2
Source1:	    gsopcast.desktop
Source2:	    gsopcast_icon.tar.bz2
Patch0:         header.diff
Patch1:         channel_filter.diff 
BuildRequires:	udisks2

%description
gsopcast is a GTK GUI front-end of the Linux command line executive of P2P TV sopcast.

Authors:
--------
    Wei Lian <lianwei3@gmail.com>
    yetist   <yetist@gmail.com>

%prep
%setup -q
cp $RPM_SOURCE_DIR/gsopcast.desktop ./src/
tar xf $RPM_SOURCE_DIR/gsopcast_icon.tar.bz2
%patch0 -p 0
%patch1 -p 1

%build
#CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS"
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
# mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/gsopcast/
# cp AUTHORS COPYING README TODO $RPM_BUILD_ROOT/usr/share/doc/packages/gsopcast/
# cd src
make install DESTDIR=$RPM_BUILD_ROOT
cp -r icons $RPM_BUILD_ROOT/usr/share/
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/gsopcast
/usr/share/locale/*
# /usr/share/apps/gsopcast/*
/usr/share/applications/gsopcast.desktop
/usr/share/pixmaps/gsopcast.png
/usr/share/icons/hicolor/*

%post
rm -rf /tmp/gsopcast
mkdir /tmp/gsopcast
cd /tmp/gsopcast
wget -T 3 -t 20 http://download.sopcast.cn/download/sp-auth.tgz
tar -zxvf sp-auth.tgz
killall -9 gsopcast
cp sp-auth/sp-sc-auth /usr/bin/
ln -s /usr/bin/sp-sc-auth /usr/bin/sp-sc
rm -rf /tmp/gsopcast

%postun
rm -f /usr/bin/sp-sc-auth
rm -f /usr/bin/sp-sc

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuild for Fedora
* Thu Jul 01 2008 - Alex Lau <avengermojo@gmail.com> 0.4.0-1
- initial spec file
