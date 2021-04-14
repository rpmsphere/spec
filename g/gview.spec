%undefine _debugsource_packages

Summary:	A simple GTK/GDK image viewer.
Name:		gview
Version:	0.9.1a
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://downloads.sourceforge.net/project/gview/gview/gview-0.9a/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	gtk2-devel
URL:		http://gview.sourceforge.net/

%description
GView is a very small, very simple, command-line operated
image viewing utility. Not packing tons of powerful features
(resize and zoom is all), GView is meant to be a replacement
for other apps such as Eye of Gnome.

%prep
%setup -q

%build
gcc -c *.c `pkg-config --cflags gtk+-2.0`
gcc -o gview *.o `pkg-config --libs gtk+-2.0` -Wl,--allow-multiple-definition

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}er
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}er.desktop
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}er.png
sed -i 's|%{name}|%{name}er|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}er.desktop 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}er
%{_datadir}/applications/%{name}er.desktop
%{_datadir}/pixmaps/%{name}er.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1a
- Rebuilt for Fedora
