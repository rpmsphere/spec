%undefine _debugsource_packages

Summary:	Disk encryption software 
Name:		veracrypt
Version:	1.24.7
Release:	1
License:	Microsoft Public License
Group:		File tools
URL:		https://www.veracrypt.fr/
Source0:	https://github.com/veracrypt/VeraCrypt/archive/VeraCrypt_1.24-Update7_Source.tar.bz2
Patch1:		veracrypt-1.0f-2-no-makeself.patch
Patch2:		veracrypt-1.0f-2-desktop.patch 
BuildRequires:	wxGTK3-devel
BuildRequires:	nasm
BuildRequires:	yasm
BuildRequires:	fuse-devel
BuildRequires:	ghostscript ImageMagick

%description
Free disk encryption software based on TrueCrypt.

%prep
%setup -qc
#%patch1 -p1
%patch2 -p1
#sed -i 's|dumpversion|dumpfullversion|' src/Makefile

%build
export CC=clang CXX=clang++
pushd src
make WX_CONFIG=wx-config-3.0
popd

pushd src/Resources/Icons
convert VeraCrypt-16x16.xpm VeraCrypt-16x16.png
convert VeraCrypt-48x48.xpm VeraCrypt-48x48.png
popd

rm -f src/Setup/Linux/usr/bin/veracrypt-uninstall.sh

%install
cd src
%make_install
install -Dm 0644 Resources/Icons/VeraCrypt-16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -Dm 0644 Resources/Icons/VeraCrypt-48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%files
%{_bindir}/*
%{_docdir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.24.7
- Rebuilt for Fedora
* Tue Oct 18 2016 Denis Silakov <denis.silakov@rosalab.ru> 1.19-1
- (9623fad) Merge pull request #4 from tremod/veracrypt:rosa2016.1
- (9623fad) Update to 1.19
* Sun Oct 18 2015 Denis Silakov <dsilakov@gmail.com> 1.16-1
- (eac346d) Updated to 1.16
