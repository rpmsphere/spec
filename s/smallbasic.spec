Summary: Small BASIC Interpreter
Name: smallbasic
Version: 12.24git
Release: 1
License: GPL
Group: Development/Languages
#Source: SmallBASIC-%{version}.tar.gz
Source: SmallBASIC-master.zip
URL: https://github.com/smallbasic/SmallBASIC
BuildRequires: gcc-c++, SDL2-devel, SDL2_image-devel, freetype-devel, vim-common, fontconfig-devel

%description
SmallBASIC is a fast and easy to learn BASIC language interpreter ideal
for everyday calculations, scripts and prototypes. SmallBASIC includes
trigonometric, matrices and algebra functions, a built in IDE, a powerful
string library, system, sound, and graphic commands along with structured
programming syntax.

%prep
%setup -q -n SmallBASIC-master

%build
sh autogen.sh
./configure --prefix=/usr --enable-sdl
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
 
%files 
%doc AUTHORS ChangeLog COPYING NEWS README*
%{_bindir}/sbasic*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/sb-desktop-128x128.png

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 12.24git
- Rebuilt for Fedora
* Sun Oct 19 2003 Kitt Tientanopajai <kitty@kitty.in.th>
- Initial RPM release
