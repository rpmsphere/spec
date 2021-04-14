%undefine _debugsource_packages

Summary:	An Integrated Development Environment for producing eLearning
Name: 		salasaga
Version: 	0.8.0.alpha5
Release: 	9.4
License:	LGPLv2+
Group:      Games/Other
URL:		http://www.salasaga.org/
Source:     http://prdownloads.sourceforge.net/salasaga/%{name}-%{version}.tar.bz2
Requires:	ming
Requires:	libgnome
Requires:	giflib
Requires:	GConf2
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	ming-devel
BuildRequires:	giflib
BuildRequires:	GConf2-devel
BuildRequires:	libgnome-devel
BuildRequires:	openal-soft-devel
BuildRequires:	udisks2

%description
Imagine a free, easy to use GUI authoring environment that helps you create visually impressive 
and actually useful learning material. The short term goal for this project is to provide such an 
environment, and we're well on the way to a first release for doing that.

%prep
%setup -q -n %{name}-0.8.0~alpha5

%build
autoconf
export CFLAGS=-Wno-error LDFLAGS=-lm
%configure
%__make

%install
rm -rf %{buildroot}
%makeinstall

# menu entry
desktop-file-install \
    --add-category="Graphics" \
    --add-category="2DGraphics" \
    --add-category="GTK" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*.desktop \
    --vendor=""

%find_lang %{name}

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%dir %{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Jul 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0.alpha5
- Rebuilt for Fedora
* Wed Apr 02 2008 Juan Luis Baptiste <jbaptiste@merlinux.org> 0.8.0-1pclos_mypclinuxos2007
- Initial import to PCLinuxOS 2008
