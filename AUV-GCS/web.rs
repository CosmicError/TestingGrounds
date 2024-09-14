/*
[package]
name = "website"
version = "0.1.0"
edition = "2021"

[dependencies]
eframe = { version = " 0.28.1", features = [
    "default",
    "__screenshot",
] }

egui-notify = "0.15.0"

# For image support:
# egui_extras = { workspace = true, features = ["default", "image"] }

env_logger = { version = "0.11.5", default-features = false, features = [
    "auto-color",
    "humantime",
] }
*/

//use std::time::Duration;

use eframe::egui; // https://docs.rs/egui/0.28.1/egui/index.html
use eframe::egui::{Pos2, Vec2};
use eframe::NativeOptions;

use egui_notify::Toasts;

/*
  TODO:
   * Video Stream // https://www.reddit.com/r/rust/comments/1d3k4bm/egui_for_video_display_in_real_time/
   * CLI / Log Viewer
   * Graphs // https://github.com/emilk/egui_plot
 */

fn main() {
    let _ = eframe::run_native(
        "AUV Control Panel",
        NativeOptions {
            viewport: egui::ViewportBuilder::default().with_inner_size([1280.0, 720.0]),
            ..Default::default()
        },
        Box::new(|_| {
            Ok(Box::<App>::default())
        }),
    );
}

struct App {
    version: String,
    toasts: Toasts,

    stream_title: String,
    stream_size: Vec2,
    stream_pos: Pos2,

    log_title: String,
    log_size: Vec2,
    log_pos: Pos2,
}

impl Default for App {
    fn default() -> Self {
        Self {
            version: "0.1.0".to_owned(),
            toasts: Toasts::default(),

            // Stream
            stream_title: "Stream".to_owned(),
            stream_size: egui::Vec2::new(300.0, 300.0),

            // https://docs.rs/egui/latest/egui/struct.Color32.html
            stream_pos: egui::pos2(16.0, 128.0),

            // Logs
            log_title: "Logs".to_owned(),
            log_size: egui::Vec2::new(300.0, 300.0),
            log_pos: egui::pos2(50.0, 128.0),
        }
    }
}

impl eframe::App for App {
    //let mut toasts = Toasts::default();

    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.label(format!("Version {}", self.version));
        });

        // https://docs.rs/egui-notify/0.15.0/egui_notify/
        //self.toasts.info("Hello world!").set_duration(Some(std::time::Duration::from_secs(5)));

        // https://docs.rs/egui/latest/egui/containers/struct.Frame.html
        // https://docs.rs/egui/latest/egui/containers/struct.Window.html
        egui::Window::new(&self.stream_title)
            .default_pos(self.stream_pos)
            .min_size(self.stream_size)
            .show(ctx, |ui| {
                ui.horizontal(|ui| {
                    ui.label("Your name: ");
                });
            });

        egui::Window::new(&self.log_title)
            .default_pos(self.log_pos)
            .min_size(self.log_size)
            .show(ctx, |ui| {
                ui.horizontal(|ui| {
                    ui.label("Your name: ");
                });
            });

        self.toasts.show(ctx);
    }
}
