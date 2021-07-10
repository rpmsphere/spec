%define _sdl_build	0

Summary:		An OpenGL port of the classic 3D Shooter game Descent 2
Name:			d2x-xl
Version:		1.18.75
Release:		1
License:		GPL
Group:			Amusements/Games/Action/Shoot
URL:			http://www.descent2.de/
Source:			%{name}-src-%{version}.7z
Source1:		%{name}.png
Source98:		hogfile.cpp
Source99:		hogfile.h
BuildRequires:	dos2unix, p7zip
BuildRequires:	gcc-c++
BuildRequires:	mesa-libGL-devel
BuildRequires:	nasm
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel

%description
D2X-XL is an OpenGL port of the classic 3D Shooter game Descent 2
for Win32, Linux and Mac OS X, containing many enhancements and
bug fixes while preserving full backwards compatibility.

D2X-XL is based on source code that was released the 14.12.1999
by Parallax Software Corporation.

%prep
%setup -q -c
7za x -y %{name}-makefiles.7z

#%__cp %{SOURCE98} io
#%__cp %{SOURCE99} include
%__sed -i -e 's|args.cpp cfile.cpp d_io.cpp|args.cpp cfile.cpp d_io.cpp hogfile.cpp|g' \
	io/Makefile.am

find . -name '_svn'      | xargs %__rm -rf
find . -name 'config*'   | xargs dos2unix
find . -name 'Makefile*' | xargs dos2unix

dos2unix    autogen.sh missing depcomp
%__chmod +x autogen.sh missing depcomp
./autogen.sh

%__chmod +x configure
%__chmod +x config.sub
%__chmod +x missing

dos2unix     COPYING
%__chmod 644 COPYING

sed -i 's|-Wall|-Wall -Wno-narrowing -lstdc++ -std=gnu++11|' configure
sed -i 's|false, -1|NULL, -1|' effects/lightning.cpp
sed -i '1i #define HAVE_STRUCT_TIMESPEC 1' libmve/mveplay.cpp
#sed -i 's|COLOR|COLOR.index|' texmap/tmapflat.cpp

%build
# SDL version (broken)
%if "%{_sdl_build}" == "1"
	%configure \
		--bindir=%{_bindir} \
		--enable-release \
		--with-opengl=no \
		--with-sharepath=%{_datadir}/%{name}
	%__make %{?jobs:-j%{jobs}}
	%__mv %{name} %{name}-sdl
	%__make clean
%endif

# GL version
%configure \
	--bindir=%{_bindir} \
	--enable-release \
	--with-opengl \
	--enable-network \
	--with-sharepath=%{_datadir}/%{name}

sed -i 's|-Werror=format-security||' */Makefile
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "%{buildroot}"
%makeinstall

%if "%{_sdl_build}" == "1"
	%__install -dm 755 %{buildroot}%{_bindir}
	%__install -m 755 %{name}-sdl %{buildroot}%{_bindir}
%endif

%__install -dm 755 %{buildroot}%{_datadir}/%{name}

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

# menu
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=D2X-XL
Name[zh_TW]=天旋地轉 2XL
Comment=An OpenGL port of the classic 3D Shooter game Descent 2
Comment[zh_TW]=D2X-XL 類似 Descent 2 的立體射擊遊戲
Exec=%{name}
Icon=%{name}
Categories=Game;Action;
EOF
%__install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%if "%{_sdl_build}" == "1"
%{_bindir}/%{name}-sdl
%endif

%changelog
* Sat Jul 03 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18.75
- Rebuilt for Fedora
* Mon Jun 06 2011 Chris LIN <chris.lin@ossii.com.tw> - 0.13.127-0.2.ossii
- Add BuildRequires: unrar
* Mon Dec 01 2008 Toni Graffy <toni@links2linux.de> - 0.13.127-0.pm.1
- update to 0.13.127
* Sat Nov 22 2008 Toni Graffy <toni@links2linux.de> - 0.13.124-0.pm.1
- update to 0.13.124
* Mon Nov 10 2008 Toni Graffy <toni@links2linux.de> - 0.13.122-0.pm.1
- update to 0.13.122
* Sat Nov 08 2008 Toni Graffy <toni@links2linux.de> - 0.13.121-0.pm.1
- update to 0.13.121
* Tue Oct 21 2008 Toni Graffy <toni@links2linux.de> - 0.13.116-0.pm.1
- update to 0.13.116
* Tue Oct 07 2008 Toni Graffy <toni@links2linux.de> - 0.13.104-0.pm.1
- update to 0.13.104
* Wed Oct 01 2008 Toni Graffy <toni@links2linux.de> - 0.13.95-0.pm.1
- update to 0.13.95
* Sat Sep 27 2008 Toni Graffy <toni@links2linux.de> - 0.13.93-0.pm.1
- update to 0.13.93
* Sat Sep 13 2008 Toni Graffy <toni@links2linux.de> - 0.13.84-0.pm.1
- update to 0.13.84
* Thu Sep 11 2008 Toni Graffy <toni@links2linux.de> - 0.13.82-0.pm.1
- update to 0.13.82
* Thu Aug 28 2008 Toni Graffy <toni@links2linux.de> - 0.13.81-0.pm.1
- update to 0.13.81
* Sat Aug 23 2008 Toni Graffy <toni@links2linux.de> - 0.13.74-0.pm.1
- update to 0.13.74
* Wed Aug 20 2008 Toni Graffy <toni@links2linux.de> - 0.13.72-0.pm.1
- update to 0.13.72
* Thu Aug 14 2008 Toni Graffy <toni@links2linux.de> - 0.13.66-0.pm.1
- update to 0.13.66
* Mon Aug 11 2008 Toni Graffy <toni@links2linux.de> - 0.13.60-0.pm.1
- update to 0.13.60
* Fri Aug 08 2008 Toni Graffy <toni@links2linux.de> - 0.13.57-0.pm.1
- update to 0.13.57
* Wed Aug 06 2008 Toni Graffy <toni@links2linux.de> - 0.13.55-0.pm.1
- update to 0.13.55
* Tue Jul 29 2008 Toni Graffy <toni@links2linux.de> - 0.13.52-0.pm.1
- update to 0.13.52
* Wed Jul 23 2008 Toni Graffy <toni@links2linux.de> - 0.13.49-0.pm.1
- update to 0.13.49
* Fri Jul 11 2008 Toni Graffy <toni@links2linux.de> - 0.13.40-0.pm.1
- update to 0.13.40
* Mon Jul 07 2008 Toni Graffy <toni@links2linux.de> - 0.13.35-0.pm.1
- update to 0.13.35
* Sat Jul 06 2008 Toni Graffy <toni@links2linux.de> - 0.13.32-0.pm.1
- update to 0.13.32
* Thu Jun 26 2008 Toni Graffy <toni@links2linux.de> - 0.13.31-0.pm.1
- update to 0.13.31
* Mon Jun 23 2008 Toni Graffy <toni@links2linux.de> - 0.13.28-0.pm.1
- update to 0.13.28
* Tue Jun 17 2008 Toni Graffy <toni@links2linux.de> - 0.13.22-0.pm.1
- update to 0.13.22
* Fri Jun 13 2008 Toni Graffy <toni@links2linux.de> - 0.13.19-0.pm.1
- update to 0.13.19
* Mon Jun 09 2008 Toni Graffy <toni@links2linux.de> - 0.13.15-0.pm.1
- update to 0.13.15
* Tue Jun 03 2008 Toni Graffy <toni@links2linux.de> - 0.13.6-0.pm.1
- update to 0.13.6
* Fri May 30 2008 Toni Graffy <toni@links2linux.de> - 0.13.3-0.pm.1
- update to 0.13.3
* Sun May 25 2008 Toni Graffy <toni@links2linux.de> - 0.12.110-0.pm.1
- update to 0.12.110
* Sun May 18 2008 Toni Graffy <toni@links2linux.de> - 0.12.99-0.pm.1
- update to 0.12.99
* Wed May 14 2008 Toni Graffy <toni@links2linux.de> - 0.12.94-0.pm.1
- update to 0.12.94
* Sun May 11 2008 Toni Graffy <toni@links2linux.de> - 0.12.92-0.pm.1
- update to 0.12.92
* Tue Apr 29 2008 Toni Graffy <toni@links2linux.de> - 0.12.88-0.pm.1
- update to 0.12.88
* Tue Apr 08 2008 Toni Graffy <toni@links2linux.de> - 0.12.75-0.pm.1
- update to 0.12.75
* Thu Mar 27 2008 Toni Graffy <toni@links2linux.de> - 0.12.67-0.pm.1
- update to 0.12.67
* Sun Mar 23 2008 Toni Graffy <toni@links2linux.de> - 0.12.65-0.pm.1
- update to 0.12.65
* Tue Mar 18 2008 Toni Graffy <toni@links2linux.de> - 0.12.60-0.pm.1
- update to 0.12.60
* Tue Mar 11 2008 Toni Graffy <toni@links2linux.de> - 0.12.55-0.pm.1
- update to 0.12.55
* Tue Feb 26 2008 Toni Graffy <toni@links2linux.de> - 0.12.44-0.pm.1
- update to 0.12.44
* Sat Feb 23 2008 Toni Graffy <toni@links2linux.de> - 0.12.40-0.pm.1
- update to 0.12.40
* Fri Feb 15 2008 Toni Graffy <toni@links2linux.de> - 0.12.27-0.pm.1
- update to 0.12.27
* Tue Feb 12 2008 Toni Graffy <toni@links2linux.de> - 0.12.21-0.pm.1
- update to 0.12.21
* Tue Feb 05 2008 Toni Graffy <toni@links2linux.de> - 0.12.8-0.pm.1
- update to 0.12.8
* Sat Feb 02 2008 Toni Graffy <toni@links2linux.de> - 0.12.1-0.pm.1
- update to 0.12.1
* Wed Jan 30 2008 Toni Graffy <toni@links2linux.de> - 0.11.123-0.pm.1
- update to 0.11.123
* Mon Jan 28 2008 Toni Graffy <toni@links2linux.de> - 0.11.120-0.pm.1
- update to 0.11.120
* Sun Jan 27 2008 Toni Graffy <toni@links2linux.de> - 0.11.119-0.pm.1
- update to 0.11.119
* Fri Jan 25 2008 Toni Graffy <toni@links2linux.de> - 0.11.116-0.pm.1
- update to 0.11.116
* Mon Jan 21 2008 Toni Graffy <toni@links2linux.de> - 0.11.110-0.pm.1
- update to 0.11.110
* Sun Jan 20 2008 Toni Graffy <toni@links2linux.de> - 0.11.109-0.pm.1
- update to 0.11.109
* Fri Jan 18 2008 Toni Graffy <toni@links2linux.de> - 0.11.107-0.pm.1
- update to 0.11.107
* Thu Jan 17 2008 Toni Graffy <toni@links2linux.de> - 0.11.105-0.pm.1
- update to 0.11.105
* Tue Jan 15 2008 Toni Graffy <toni@links2linux.de> - 0.11.101-0.pm.1
- update to 0.11.101
* Mon Jan 14 2008 Toni Graffy <toni@links2linux.de> - 0.11.99-0.pm.1
- update to 0.11.99
* Thu Jan 10 2008 Toni Graffy <toni@links2linux.de> - 0.11.97-0.pm.1
- update to 0.11.97
* Tue Jan 08 2008 Toni Graffy <toni@links2linux.de> - 0.11.95-0.pm.1
- update to 0.11.95
* Sat Jan 05 2008 Toni Graffy <toni@links2linux.de> - 0.11.93-0.pm.1
- update to 0.11.93
* Wed Jan 02 2008 Toni Graffy <toni@links2linux.de> - 0.11.92-0.pm.1
- update to 0.11.92
* Fri Dec 28 2007 Toni Graffy <toni@links2linux.de> - 0.11.88-0.pm.1
- update to 0.11.88
* Thu Dec 27 2007 Toni Graffy <toni@links2linux.de> - 0.11.86-0.pm.1
- update to 0.11.86
* Tue Dec 25 2007 Toni Graffy <toni@links2linux.de> - 0.11.84-0.pm.1
- update to 0.11.84
* Sat Dec 22 2007 Toni Graffy <toni@links2linux.de> - 0.11.82-0.pm.1
- update to 0.11.82
* Fri Dec 21 2007 Toni Graffy <toni@links2linux.de> - 0.11.81-0.pm.1
- update to 0.11.81
* Thu Dec 20 2007 Toni Graffy <toni@links2linux.de> - 0.11.80-0.pm.1
- update to 0.11.80
* Tue Dec 18 2007 Toni Graffy <toni@links2linux.de> - 0.11.77-0.pm.1
- update to 0.11.77
* Sun Dec 16 2007 Toni Graffy <toni@links2linux.de> - 0.11.76-0.pm.1
- update to 0.11.76
* Sat Dec 15 2007 Toni Graffy <toni@links2linux.de> - 0.11.74-0.pm.1
- update to 0.11.74
* Fri Dec 14 2007 Toni Graffy <toni@links2linux.de> - 0.11.72-0.pm.1
- update to 0.11.72
* Thu Dec 13 2007 Toni Graffy <toni@links2linux.de> - 0.11.71-0.pm.1
- initial package 0.11.71
