%undefine _debugsource_packages

Summary:	A game of Belote
Name:		belooted
Version:	0.1.4
Release:	9.1
License:	GPL v2
Group:		Amusements/Games
Source0:	http://boby.joe.free.fr/dev/belooted/files/%{name}-%{version}.tar.gz
Source1:	belooted-background-default.png
URL:		http://boby.joe.free.fr/dev/belooted/
BuildRequires:	gawk
BuildRequires:	perl-XML-Parser
BuildRequires:	gtk2-devel >= 2.8.0
BuildRequires:	desktop-file-utils

%description
Belote is a popular 32-card trick-taking game played in France.
It derived around 1920, probably via Clobyosh, from Klaverjassen,
a game played since at least the 1600s in the Netherlands.
Closely related games are played throughout the world.
Details: http://en.wikipedia.org/wiki/Belote

%prep
%setup -q
cp %{SOURCE1} pixmaps/
sed -i -e 's!background-gnome.jpg!belooted-background-default.png!g' src/options.c

%build
export CFLAGS="-lm -fPIC"
%configure 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} install DESTDIR=%{buildroot}

%{__install} -p -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/belooted/
%{__rm} -rf %{buildroot}%{_datadir}/pixmaps/belooted/background-gnome.jpg

desktop-file-install --vendor="" \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{buildroot}%{_datadir}/applications/belooted.desktop

%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Mon Jul 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4
- Rebuilt for Fedora
* Wed Aug 5 2009 Radu-Cristian Fotescu <info [AT] beranger [DOT] org>
- Initial release for this repo. No translations (English-only)
