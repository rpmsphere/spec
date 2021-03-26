Summary:	A networked Chinese Checkers game
Name:		cheech
Version:	0.8
Release:	1
License:	GPL
Group:		Amusements/Games
URL:		http://cheech.sourceforge.net/
BuildRequires:	gtkmm24-devel, gnet2-devel, libsigc++20-devel
Source:		http://prdownloads.sourceforge.net/cheech/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-utility.patch

%description
cheech is a portable, multiplayer, networked Chinese Checkers game.
It currently lets you play chinese checkers over a network against
any combination of up to 5 other people or computer players.

cheech is built by Ben Levitt and based on gchch by Loban A. Rahman. 

%prep
%setup -q
%patch0
#libsigc++ 2.0 跟 1.2 的差別 namespace 不同
sed -i 's/SigC::slot/sigc::mem_fun/g' src/*    
sed -i 's|sigc++/compatibility.h|c++/7/parallel/compatibility.h|' src/*
sed -i '1i #include <glibmm/main.h>' src/bot_base.cc
sed -i 's|erase_selection(Gtk::Clipboard::get())|erase_selection(true, true)|' src/main_win.cc
sed -i '1i #include <unistd.h>' src/utility.cc

%build
./autogen.sh
%configure 
#SIGC_LIBS=" -lsigc-2.0 -lsigc-1.2"
sed -i 's|CFLAGS =|CFLAGS = -fpermissive|' src/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
mv $RPM_BUILD_ROOT/usr/doc/cheech/* $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_datadir}/doc/%{name}-%{version}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuild for Fedora
* Thu Jun 09 2011 Chris Lin <chris.lin@ossii.com.tw> - 0.8-2.ossii
- Fix sigc++ issues
