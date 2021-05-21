Name:           lmc
URL:            https://github.com/lanmessenger/lanmessenger
Group:          Productivity/Networking/Instant Messenger
Summary:        LAN Messenger Instant messaging client
Version:        1.2.35
#Version:        1.2.39
Release:        13.1
License:        GPL-3.0
Source0:        http://downloads.sourceforge.net/project/lanmsngr/%{version}/%{name}-%{version}-src.zip
Source1:        %{name}-%{version}-lang.zip
Patch0:         %{name}-qtlocalpeer.patch
Patch1:         %{name}-buildx11.patch
Patch2:         %{name}-lan-messenger.patch
Patch3:         %{name}-lmc.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  openssl-devel
BuildRequires:  qt4-devel qt4-x11 qtwebkit-devel phonon-devel kdelibs-devel
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  unzip
BuildRequires:  qca2 udisks2

%description
LAN Messenger is a free and open source cross-platform instant messaging
application for communication over a local network. It does not require a
server. A number of useful features including event notifications, file transfer
and message logging are provided.
Authors: Qualia Digital Solutions <qualiatech@gmail.com>

%prep
%setup -q -c
%patch0
%patch1
%patch2
%patch3
#if %{fedora}>20
#sed -i 's|#include <QWebView>|#include <QtWebKitWidgets/QWebView>|' lmc/src/settingsdialog.cpp lmc/src/messagelog.h
#endif

%build
#pushd lmcapp/src
#qmake-qt4 QMAKE_CFLAGS+="%optflags -std=gnu99" QMAKE_CXXFLAGS+="%optflags -std=c++0x"
#make
#popd
pushd lmc/src
qmake-qt4 QMAKE_CFLAGS+="%optflags -std=gnu99" QMAKE_CXXFLAGS+="%optflags -std=c++0x"
make

%install
install -d -m 755 %{buildroot}%{_libdir}/%{name}
pushd lmc/src
chmod 755 ./scripts/buildx11
sed -i 2i"QTDIR=%{_libdir}\nSSLDIR=/%{_lib}" scripts/buildx11
./scripts/buildx11 %{buildroot}%{_libdir}/%{name}
popd
install -m 0755 lmc/release/lan-messenger %{buildroot}%{_libdir}/%{name}/
install -D -m 0644 lmc/setup/x11/package/usr/share/applications/lmc.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
convert lmc/src/resources/icons/%{name}.ico\[0\] %{name}.png
install -D -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,72x72,96x96,128x128,192x192,256x256}/apps
for size in 16x16 22x22 24x24 32x32 36x36 48x48 64x64 72x72 96x96 128x128 192x192 256x256
do
if [ "$size" = 256x256 ]
then
install -D -m 0644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{name}.png
continue
fi
convert %{buildroot}%{_datadir}/pixmaps/%{name}.png -resize $size %{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{name}.png
done
install -d -m 755 %{buildroot}%{_bindir}
ln -sfv %{_libdir}/%{name}/lan-messenger.sh %{buildroot}%{_bindir}/%{name}

unzip %{SOURCE1} -d %{buildroot}%{_libdir}/%{name}/lang

%files
%doc README.TXT
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.35
- Rebuilt for Fedora
* Fri Dec 21 2012 fa0sck@gmail.com
- Initial package for openSUSE - ver 1.2.35
