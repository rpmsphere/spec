Summary:	Pretty version of df(1) command
Summary(pl):	Ładna wersja polecenia df(1)
Name:		discus
Version:	0.2.9
Release:	2.1
License:	GPL
Group:		Applications/Console
Source0:	http://www.raincrazy.com/software/discus/%{name}-%{version}.tar.gz
URL:		http://www.raincrazy.com/software/discus/
Requires:	python2
BuildArch:	noarch

%description
Discus aims to make df prettier, with features such as color, graphs,
and smart formatting of numbers (automatically choosing the most
suitable size from kilobytes, megabytes, gigabytes, or terabytes). If
you don't want Discus deciding the best sizes, you can also choose
your own increments, along with specifying the number of decimal
places you'd like to see.

%description -l pl
Discus zamierza uczynić df piękniejszym, poprzez kolor, wykresy i
eleganckie formatowanie liczb (automatycznie wybierając najbardziej
odpowiednią wielkość z kilobajtów, megabajtów, gigabajtów lub
terabajtów). Jeżeli nie chcesz, żeby Discus decydował o najlepszej
wielkości, możesz też wybrać własne przyrosty, po przez podanie
liczby miejsc dziesiętnych, które chciałbyś widzieć.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}
install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}rc	$RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.1	$RPM_BUILD_ROOT%{_mandir}/man1

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS BUGS changelog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}rc
%{_mandir}/man1/*

%changelog
* Thu Oct 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.9
- Rebuilt for Fedora
* Mon Jan 26 2004 wolf <feedback@pld-linux.org>
- proper requires
* Fri Nov 14 2003 qboosh <feedback@pld-linux.org>
- cleanups
* Fri Nov 14 2003 twittner <feedback@pld-linux.org>
- new.
