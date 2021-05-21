Name:           lximedia
Version:        0.3.4
Release:        1
Summary:        DLNA media server
License:        GPL-3.0
Group:          Development/Libraries/X11
URL:            http://sourceforge.net/projects/lximedia/
Source:		%{name}_%{version}-1.tar.gz
Source1:	%{name}.sysvinit
Patch:		%{name}-notests.patch
BuildRequires:	doxygen
BuildRequires:	gcc-c++ make
BuildRequires:  ffmpeg-devel
BuildRequires:  qt4-devel
BuildRequires:  libexif-devel
BuildRequires:  libdvdnav-devel
#BuildRequires:  libwbclient
BuildRequires:  libsmbclient-devel
BuildRequires:  pulseaudio-libs-devel alsa-lib-devel
BuildRequires:  qtwebkit-devel
#BuildRequires:  amrnb-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel

%description
A media server that streams multimedia contents to network devices compatible
with the DLNA protocol. It's also able to transcode files on the fly to improve
format compatibility.

%prep
%setup -q
%patch -p1

%ifarch x86_64
find ./ -type f -exec sed -i 's|target.path = /usr/lib|target.path = /usr/lib64|' {} \;
find ./ -type f -exec sed -i 's|usr/lib/|usr/lib64/|' {} \;
%endif

#sed -i '206,208d' src/lxistream/plugins/ffmpeg/datadecoder.cpp
#sed -i 's|libsmbclient\.h|samba-4.0/libsmbclient.h|' src/lxistream/plugins/smbclient/smbfilesystem.cpp

#cd src/lxistream/plugins/ffmpeg
#qmake-qt4
#sed -i 's|-I/usr/include |-I/usr/include -I/usr/include/ffmpeg -fpermissive |' Makefile

%build
qmake-qt4 -recursive
sed -i 's|-I/usr/include |-I/usr/include -I/usr/include/ffmpeg |' src/lxistream/plugins/ffmpeg/Makefile
sed -i 's|-Wall|-Wall -fpermissive|' src/lxistream/*/Makefile src/lxistream/plugins/*/Makefile
%{__make} %{?jobs:-j %jobs}

%install
%makeinstall INSTALL_ROOT=%buildroot
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/lximcbackend
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_initrddir}/lximcbackend %{buildroot}%{_sbindir}/rclximcbackend

%pre
getent group lximediacenter >/dev/null || groupadd -r lximediacenter
getent passwd lximediacenter >/dev/null || useradd -r -g lximediacenter -M -d /var/lib/lximediacenter -s /sbin/nologin -c "user for lximcbackend" lximediacenter
install -o lximediacenter -g lximediacenter -d /var/lib/lximediacenter
exit 0

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING
%_bindir/*
%_libdir/libLXi*
%_libdir/lximedia0/*
%_initrddir/lximcbackend
%_sbindir/rclximcbackend

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuilt for Fedora
* Sat Apr 21 2012 Julian Weissgerber <sloevenh1@googlemail.com> - 0.3.3-1
- SysV script
* Thu Apr 19 2012 Julian Weissgerber <sloevenh1@googlemail.com> - 0.3.3-0
- Initial package
