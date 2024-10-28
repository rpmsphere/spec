Name: xvnkb
Version: 0.2.11
Release: 1.1
License: GPL
Summary: Vietnamese keyboard input for X-Window
Group: System/Internationalization
URL: https://xvnkb.sourceforge.net/
Vendor: LandShark Networks
Source: https://xvnkb.sourceforge.net/%{name}-%{version}.tar.gz
BuildRequires: libX11-devel libXft-devel

%description
xvnkb is a Vietnamese keyboard input for X-Window. It provides an 
useful way for editing Vietnamese on X-Window environment with 
popular input methods and charsets. 

xvnkb 0.2.x support UTF-8 Encoding ;). Good news, eh?

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
./configure --use-extstrocke --use-prostroke --use-abcstroke
sed -i 's|X11R6/||g' tools/Makefile*
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name}.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install -m 755 tools/xvnkb_ctrl $RPM_BUILD_ROOT%{_bindir}
install -m 755 scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%post
VERSION="%{version}"
OL=`echo $LD_PRELOAD | grep xvnkb.so`
LD="/etc/ld.so.preload"
SO="/lib/xvnkb.so"
XVNKB_CORE="$SO.$VERSION"
unset LD_PRELOAD N
while [ -f $XVNKB_CORE ]; do
        if [ "$N" = "" ]; then
                N=1
        else
                N=$((N + 1))
        fi
        XVNKB_CORE="$SO.$VERSION-$N"
done
cp %{_libdir}/xvnkb.so.$VERSION $XVNKB_CORE
chattr +i $XVNKB_CORE
if [ -f "$LD" ]; then
        grep -v xvnkb.so $LD > $LD.xvnkb
        /bin/mv -f $LD.xvnkb $LD
fi
echo "$XVNKB_CORE" >> $LD

if [ "$LANG" = "C" ]; then
        LANG="en_US"
fi

if [ "`echo $LANG | grep UTF-8`" = "" ]; then
        echo "If you want to input Vietnamese Unicode, please run"
        echo
        echo "  # $PREFIX/bin/xvnkb_localeconf.sh $LANG.UTF-8"
        echo
        echo "and set your LANG to $LANG.UTF-8."
        echo "See xvnkb documents at %{_datadir}/doc/xvnkb for more information."
fi

if [ "$OL" != "" ]; then
        echo -e "\\033[1;31m"
        echo "* NOTICE:"
        echo "You are using LD_PRELOAD to load xvnkb core. If you set it somewhere else"
        echo "(e.g. /etc/profile, /etc/bashrc, ~/.bash_profile, ~/.bashrc, ~/.xinitrc)"
        echo "by yourself, please remove it also!"
        echo -e "\\033[0;39m"
fi

echo "You can use xvnkb now!  If you are using X, please restart your Window Manager."
echo "It will load xvnkb core control automatically for you and affect to all"
echo "applications.  Right now, xvnkb core control can affect to new starting"
echo "applications only.  Run \"xvnkb\" to control status."

%files
%doc AUTHORS ChangeLog README* INSTALL* TODO THANKS COPYING 
%doc contrib/profile scripts/*.sh doc/* 
%{_bindir}/%{name}*
%{_libdir}/%{name}*
%{_datadir}/%{name}

%changelog
* Wed Dec 17 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.11
- Rebuilt for Fedora
* Sat Jan 14 2006 LandShark BuildSys <BuildSys[AT]LandShark.Net>
- Initial CentOS 4 build.
