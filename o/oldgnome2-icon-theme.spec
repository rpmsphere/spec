%define theme_name OldGNOME2

Summary:        %{theme_name} icon theme
Name:           oldgnome2-icon-theme
Version:        0.1.1
Release:        1.1
License:        GPL2+
Group:          User Interface/Desktops
URL:            https://eqlovelace.deviantart.com/art/Old-GNOME2-Icon-Theme-192943815
Source0:        %{theme_name}.tar.gz
BuildArch:      noarch

%description
I personally don't much care for the post-Tango gnome icon theme that first
started coming out around the 2.16 release. The edges are much less sharp,
and the changed aesthetic just doesn't appeal to me. Unfortunately, 2.16 was
also the first release to use a newer icon naming system that led to many
icons simply not working if you merely copied over the old icon theme.
So i've taken matters into my own hands

This is the old pre-2.16 Gnome icon theme, modified and repackaged to work
with modern (as of 2.32) Gnome desktops. I did not create any of these icons,
rather i merely collected them from various sources (gnome-icon-theme,
individual gnome apps) and threw a bunch of symlinks in for compatability.
It's been a personal work-in-progress for several years, and i'm releasing it
now in case anyone else shares my sense of aesthetics.

It's got pretty good (roughly 90%) coverage of even a current gnome desktop,
without having drawn any new icons, though in future releases, i may attempt
to modify existing icons in here (as well as scrounging up others from past
software releases) to get a wider coverage. I'm also considering including
details such as the pre-2.8 trash icon (The one at a 3/4 viewing angle) if
anyone wants that.

I've also enclosed a small patch to Nautilus, to enable the use of the old
75% (36x36 pixel) icon zoom that was used in older releases, to get a more
authentic experience :)

Reports of missing icons, or requests for more app icons (I've snagged a
number of common ones already) are welcome.

%prep
%setup -q -n %{theme_name}
rm icon-theme.cache

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
