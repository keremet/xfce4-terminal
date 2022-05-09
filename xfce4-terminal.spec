Name: xfce4-terminal
Version: 10.0.0
Release: alt1

Summary: Terminal emulator application for Xfce
Summary (ru_RU.UTF-8): Эмулятор терминала для Xfce
License: GPLv2+
Group: Terminals
Url: https://docs.xfce.org/apps/terminal/start
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: https://gitlab.xfce.org/apps/xfce4-terminal.git
Source: %name-%version.tar

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-gtk3-devel
BuildPreReq: gtk-doc
BuildRequires: libpcre2-devel

# Automatically added by buildreq on Fri Aug 07 2009
BuildRequires: docbook-dtds docbook-style-xsl intltool libSM-devel libdbus-glib-devel libvte3-devel time xorg-cf-files

Requires: xfce4-common

Obsoletes: Terminal < %version
Provides: Terminal = %version-%release

%define _unpackaged_files_terminate_build 1

%description
This is the xfce4-terminal emulator application. xfce4-terminal is
a lightweight and easy to use terminal emulator for X windowing system
with some new ideas and features that makes it unique among X terminal
emulators.

%description -l ru_RU.UTF-8
xfce4-terminal - легкий и удобный эмулятор терминала для Xfce.

%prep
%setup

# Don't use git tag in version.
%xfce4_drop_gitvtag terminal_version_tag configure.ac.in

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-gen-doc \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md NEWS THANKS
%_bindir/*
%_man1dir/*
%_datadir/xfce4/terminal
%_datadir/gnome-control-center/default-apps/%name-default-apps.xml
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%changelog
* Mon May 09 2022 Andrey Sokolov <keremet@altlinux.org> 10.0.0-alt1
- Initial build for Sisyphus
