BuildRequires:			libX11-devel
Name:			gmemusage
Summary:		Graphically shows memory usage
Version:		0.2
Release:		69.1
Group:          	System/Monitoring
License:		GPL
Source:			%{name}-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:			http://oss.sgi.com/projects/gmemusage/
BuildRequires:		desktop-file-utils
Requires:		hicolor-icon-theme
BuildRequires:		hicolor-icon-theme
Patch0:			%{name}-%{version}-headers.diff

%description
Graphically shows memory usage.

%prep
%setup -q
%patch0

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" LIBX11DIR="-L %{_prefix}/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -D -m755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -D -m644 contrib/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -D -m644 contrib/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install                                    \
 --delete-original                                      \
 --vendor ""                                            \
 --dir $RPM_BUILD_ROOT%{_datadir}/applications          \
 --add-category System                                  \
 --add-category Monitor                                 \
 $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%doc ChangeLog COPYING NEWS README TODO CREDITS
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
