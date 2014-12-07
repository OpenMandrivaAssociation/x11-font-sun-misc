Name: x11-font-sun-misc
Version: 1.0.3
Release: 11
Summary: Xorg X11 font sun-misc
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-sun-misc-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.2
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font sun-misc

%prep
%setup -q -n font-sun-misc-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/misc

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/misc/fonts.scale

%post
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%postun
mkfontscale %{_datadir}/fonts/misc
mkfontdir %{_datadir}/fonts/misc

%files
%doc COPYING
%{_datadir}/fonts/misc/olcursor.pcf.gz
%{_datadir}/fonts/misc/olgl*.pcf.gz


